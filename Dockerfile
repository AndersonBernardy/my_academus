FROM python:3.7

WORKDIR /usr/src/app
COPY . .

RUN apt update
RUN apt install libmariadbclient-dev

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]