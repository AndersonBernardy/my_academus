FROM django-mariadb-base

WORKDIR /home
COPY ./my_academus .

CMD ["python3", "manage.py", "runserver", "my-academus-app:8000"]