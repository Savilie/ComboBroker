FROM nginx:1.27.1

WORKDIR /app/frontend

RUN chown nginx:nginx /var/cache/nginx/

RUN rm -f /etc/nginx/conf.d/default.conf || true

COPY nginx/nginx.conf /etc/nginx/conf.d

COPY nginx/proxy_params /etc/nginx

# COPY index.html .

RUN apt-get update && apt-get install -y npm

COPY frontend .

RUN npm install 

RUN npm run build
