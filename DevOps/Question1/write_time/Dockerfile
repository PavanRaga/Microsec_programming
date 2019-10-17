# FROM ubuntu:latest
# MAINTAINER pavan.raga98@gmail.com

# RUN apt-get update && apt-get -y install python cron
# # #RUN mkdir /app
# # WORKDIR /app
# ADD write_time.py /usr/bin/write_time.py
# RUN chmod +x /usr/bin/write_time.py

# COPY cron_write_time /etc/cron.d/cron_write_time
# RUN chmod 0644 /etc/cron.d/cron_write_time
# RUN crontab /etc/cron.d/cron_write_time
# RUN touch /var/log/cron.log
# CMD ["cron", "-f"]


# # ADD cron.sh /usr/bin/cron.sh
# # RUN chmod +x /usr/bin/cron.sh
# # ADD ./cron_write_time /etc/cron.d/cron-jobs
# # RUN chmod 0644 /etc/cron.d/cron-jobs
# # RUN touch /var/log/cron.log

# # ENTRYPOINT ["/bin/sh", "/usr/bin/cron.sh"]


# # ADD cron_write_time /etc/cron.d/my-cron
# # RUN chmod 0644 /etc/cron.d/my-cron
# # RUN chmod a+x write_time.py
# # RUN crontab cron_write_time
# # ENTRYPOINT cron -f

FROM ubuntu:16.04
RUN mkdir /app
ADD write_time.py /
USER root
RUN apt-get update && \
    apt-get install -y python cron && \
    chmod +x /write_time.py && \
    (crontab -l 2>/dev/null; echo "*/2 * * * * cd / && /usr/bin/python /write_time.py >> test.out") | crontab -
CMD cron -f