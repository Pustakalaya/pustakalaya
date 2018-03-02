FROM postgres:9.6

ENV APP_ROOT /src
WORKDIR ${APP_ROOT}
#RUN mkdir -p  /script && > /etc/cron.d/pg_backup-cron && echo "*/5 * * * * /script/autopgsqlbackup" >> /etc/cron.d/pg_backup-cron
ADD src/script.d/autopgsqlbackup /script/

RUN chmod +x /script/autopgsqlbackup
