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

RUN apt update -qq && \
    apt install -y --no-install-recommends locales tzdata && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    locale-gen C.UTF-8 && update-locale LANG=C.UTF-8 LC_ALL=C.UTF-8 && \
    useradd --home /home/non-root non-root && \
    apt install -y --no-install-recommends gcc libc6-dev libcurl4-openssl-dev libssl-dev

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

RUN apt purge -y gcc libc6-dev libcurl4-openssl-dev libssl-dev && apt autoremove -y && \ 
    apt clean -y && rm -rf /var/lib/apt/lists/*

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
