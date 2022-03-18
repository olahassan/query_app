FROM python:alpine3.14

ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=test02
ENV VERSION=1.0
ENV PARTICIPANTS=2
ENV BASEURL=http://www.boredapi.com/api/activity?

WORKDIR /src

COPY requirements.txt ./requirements.txt

RUN  pip install --no-cache-dir --upgrade -r requirements.txt

RUN apk add dos2unix

COPY . .

RUN dos2unix app/*

EXPOSE 9000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "2" ]
