#!/usr/bin/env sh
envsubst '${NGINX_STATIC_FOLDER} ${NGINX_WORKERS} ${NGINX_SERVER_APP} ${NGINX_ACCEPT_MUTEX} ${NGINX_ACCESS_LOG} ${NGINX_LOG_LEVEL} ${NGINX_TIMEOUT}' < nginx.conf > /etc/nginx/nginx.conf

nginx -g "daemon off;"