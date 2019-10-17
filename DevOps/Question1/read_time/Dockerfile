FROM ubuntu:16.04
ADD read_diff_time.py /
USER root
RUN apt-get update && \
    apt-get install -y python-pip python-dev curl && pip install flask &&\
    chmod +x /read_diff_time.py
EXPOSE 5000
CMD /usr/bin/python /read_diff_time.py