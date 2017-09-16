FROM python:3.6

EXPOSE 7001

RUN pip install django==1.11.5

COPY pyladiesdjango /src/
WORKDIR /src

CMD ["python", "manage.py", "runserver", "0.0.0.0:7001"]
