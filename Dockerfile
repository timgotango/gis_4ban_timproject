FROM python:3.9.0

WORKDIR /home/

RUN echo 'AmuMal1'

RUN git clone https://github.com/timgotango/gis_4ban_timproject.git

WORKDIR /home/gis_4ban_timproject/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=timproject.settings.deploy && python manage.py migrate --settings=timproject.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=timproject.settings.deploy timproject.wsgi --bind 0.0.0.0:8000"]