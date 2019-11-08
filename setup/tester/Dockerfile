FROM django-mariadb-base

COPY ./setup/drivers/geckodriver /usr/bin/geckodriver

COPY ./setup/tester/requirements.txt ./
RUN pip3 install -r requirements.txt

CMD ["bash"]