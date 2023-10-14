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