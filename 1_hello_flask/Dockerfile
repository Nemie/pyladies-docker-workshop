FROM python:3.6

EXPOSE 7000

RUN pip install Flask==0.12.2

COPY hello.py /src/
WORKDIR /src

CMD ["python", "hello.py"]
