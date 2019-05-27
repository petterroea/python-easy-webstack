FROM python:3.6

RUN mkdir -p /srv/easy_webserver && groupadd -r easy_webserver && useradd -r -g easy_webserver easy_webserver; \
chown easy_webserver:easy_webserver /srv/easy_webserver

WORKDIR /srv/easy_webserver
COPY . /srv/easy_webserver
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x wait-for-it.sh
#RUN rm docker-pyramid.ini
RUN pip install -e . && pip install psycopg2; \
rm -r easy_webserver; mv alembic-docker.ini alembic.ini; \
chmod +x /srv/easy_webserver/docker-startup.sh && \
mkdir /uploads && chown easy_webserver /uploads

USER easy_webserver
#EXPOSE 6543

ENV POSTGRES_ENV_PASSWORD example

ENTRYPOINT ["bash",  "/srv/easy_webserver/docker-startup.sh"]
CMD ["pserve"]