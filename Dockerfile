ARG USER=non-root
ARG EXTRA_PKGS="gcc libc6-dev"


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

ARG USER
ARG EXTRA_PKGS
ARG GIT_COMMIT

ENV TZ=America/Sao_Paulo \
    LC_ALL=pt_BR.UTF-8 \
    LC_CTYPE=pt_BR.UTF-8 \
    LANG=pt_BR.UTF-8 \
    LANGUAGE=pt_BR.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PYTHONWARNINGS="ignore:Unverified HTTPS request" \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt update -qq && \
    apt install -y --no-install-recommends locales tzdata && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen pt_BR.UTF-8 && update-locale LANG=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8 && \
    useradd --home /home/${USER} ${USER} && \
    apt install -y --no-install-recommends ${EXTRA_PKGS} libcurl4-openssl-dev libssl-dev

USER ${USER}
WORKDIR /home/${USER}

ENV GIT_COMMIT=${GIT_COMMIT} \
    USER=${USER} \
    HOME=/home/${USER} \
    PATH="/home/${USER}/.local/bin:${PATH}" \
    FLASK_APP=server.web

COPY --chown=${USER}:${USER} ./requirements.txt ./requirements.txt

RUN pip install --user -r ./requirements.txt && \
    pip cache purge && \
    rm -Rf ./.cache && \
    rm ./requirements.txt

USER root

RUN apt purge -y ${EXTRA_PKGS} && apt autoremove -y && \ 
    apt clean -y && rm -rf /var/lib/apt/lists/*

USER ${USER}
WORKDIR /home/${USER}

COPY --chown=${USER}:${USER} ./client/pages ./client/pages
COPY --chown=${USER}:${USER} ./server ./server
COPY --from=nodejs_builder --chown=${USER}:${USER} /var/nodejs-temp/public ./client/public

# ---- NGINX Release Image ----
FROM nginx:1.25.0-bullseye
ARG GIT_COMMIT

ENV GIT_COMMIT=$GIT_COMMIT \
    NGINX_WORKERS=1 \
    NGINX_ACCEPT_MUTEX=off \
    NGINX_ACCESS_LOG=off

RUN apt -qq update && \
    apt install --no-install-recommends -y locales tzdata ssl-cert && \ 
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && update-locale LANG=pt_BR.UTF-8 && \
    apt install --no-install-recommends -y nginx-extras && \
    rm -r /var/lib/apt/lists/* && apt clean

COPY [ "./scripts/nginx.conf", "./scripts/nginx.sh", "./" ]

CMD [ "/bin/bash", "./nginx.sh" ]
