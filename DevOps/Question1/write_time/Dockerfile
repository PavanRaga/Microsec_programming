FROM ubuntu:16.04
MAINTAINER pavan.raga98@gmail.com
RUN mkdir /app
ADD write_time.py /
USER root
RUN apt-get update && \
    apt-get install -y python cron && \
    chmod +x /write_time.py && \
    (crontab -l 2>/dev/null; echo "*/2 * * * * cd / && /usr/bin/python /write_time.py >> test.out") | crontab -
CMD cron -f