FROM python:3.6

WORKDIR /app

COPY source/requirements.txt ./

RUN pip install -r requirements.txt

COPY source /app

