FROM python:3.10

#Install OS Modules
RUN apt update -y && \
    apt install telnet -y && \
    rm -r -rf /var/lib/apt/lists/*

#Copy source code
RUN mkdir -p /data-copier
COPY app /data-copier/app
COPY requirements.txt /data-copier

#Install application dependancies
RUN pip install -r /data-copier/requirements.txt
