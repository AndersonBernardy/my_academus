FROM python:3.7

RUN apt-get update; apt-get install libmariadbclient-dev -y

COPY ./setup/base/requirements.txt ./
RUN pip3 install -r requirements.txt
