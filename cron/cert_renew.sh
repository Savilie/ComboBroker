COMPOSE="/usr/local/bin/docker-compose --no-ansi"

cd /home/ComboBroker/
$COMPOSE run certbot renew --dry-run && \
$COMPOSE kill -s SIGHUP nginx
