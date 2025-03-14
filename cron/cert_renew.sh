COMPOSE="/usr/local/bin/docker-compose --no-ansi"

cd /home/ComboBroker/
$COMPOSE run certbot renew && \
$COMPOSE kill -s SIGHUP nginx
