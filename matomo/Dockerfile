FROM matomo:5

COPY entrypoint.sh /entrypoint-railway.sh
RUN chmod +x /entrypoint-railway.sh

ENTRYPOINT ["/entrypoint-railway.sh"]
