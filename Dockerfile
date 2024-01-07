# ---- Node.js Builder Image ----
FROM node:14.19.0-bullseye AS nodejs_builder

COPY ./client /var/nodejs-temp

RUN cd /var/nodejs-temp && \
    rm -Rf ./node_modules && \
    npm install

RUN cd /var/nodejs-temp && \
    NODE_ENV=production npm run build

# ---- Python Image ----
FROM python:3.11.6-slim-bookworm as app_release

ENV TZ=America/Sao_Paulo \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    LANGUAGE=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PYTHONWARNINGS="ignore:Unverified HTTPS request" \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set the locale
RUN apt-get update && apt-get install -y locales && \
    sed -i -e 's/# \(en_US\.UTF-8\)/\1/' /etc/locale.gen && \
    locale-gen

RUN useradd --create-home --shell /bin/bash non-root
USER non-root
WORKDIR /home/non-root

ENV GIT_COMMIT=${GIT_COMMIT} \
    USER=non-root \
    HOME=/home/non-root \
    PATH="/home/non-root/.local/bin:${PATH}" \
    FLASK_APP=server.web

COPY --chown=non-root:non-root ./requirements.txt ./requirements.txt

RUN pip install --user -r ./requirements.txt && \
    pip cache purge && \
    rm -Rf ./.cache && \
    rm ./requirements.txt

USER root

RUN apt-get purge -y locales && apt-get autoremove -y && \ 
    apt-get clean -y && rm -rf /var/lib/apt/lists/*

USER non-root
WORKDIR /home/non-root

COPY --chown=non-root:non-root ./client/pages ./client/pages
COPY --chown=non-root:non-root ./server ./server
COPY --from=nodejs_builder --chown=non-root:non-root /var/nodejs-temp/public ./client/public

# ---- Application Services ----
# Add the following lines to the Dockerfile to include services

# Service 1: aeroespacial-site-service
CMD gunicorn -w 2 'server.web:app' -b '0.0.0.0:5000'

# Service 2: aeroespacial-worker-service
CMD celery -A server.worker worker --concurrency=2 -B --loglevel=ERROR -E
