FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt
RUN mkdir /app/src

COPY src/ /app/src/

WORKDIR /app/src

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--master", "-p", "4", "-w", "api:app"]
