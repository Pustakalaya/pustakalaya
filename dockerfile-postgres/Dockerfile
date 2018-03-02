FROM postgres:9.6

RUN mkdir -p  /pg_backups && > /etc/cron.d/pg_backup-cron && echo "*/5 * * * * /pg_backups/autopgsqlbackup" >> /etc/cron.d/pg_backup-cron
ADD ./script.d/autopgsqlbackup /pg_backups/
RUN chmod +x /pg_backups/autopgsqlbackup
