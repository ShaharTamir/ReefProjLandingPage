FROM nginx

WORKDIR /usr/app
COPY nginx.conf /etc/nginx/nginx.conf
COPY 75C693127BE7A19EA81AB0460381508D.txt ./
COPY private.key ./
COPY certificate.crt /etc/ssl/ssl-bundle.crt
