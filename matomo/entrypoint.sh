#!/bin/sh
# Railway injects $PORT — Apache defaults to 80, so we patch it at runtime
PORT="${PORT:-80}"
sed -i "s/Listen 80/Listen ${PORT}/" /etc/apache2/ports.conf
sed -i "s/<VirtualHost \*:80>/<VirtualHost *:${PORT}>/" /etc/apache2/sites-enabled/*.conf 2>/dev/null || true
exec /entrypoint.sh apache2-foreground
