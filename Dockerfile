FROM python:3.9.0

WORKDIR /home/

RUN echo 'Amu Mal'

RUN git clone https://github.com/timgotango/gis_4ban_timproject.git

WORKDIR /home/gis_4ban_timproject/

RUN echo "SECRET_KEY=django-insecure-&rh2bpv)h-ra(qfjfdbgam2ryt2g5m@w)ebzmhs4g6c$8*^4&(" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "timproject.wsgi", "--bind", "0.0.0.0:8000"]