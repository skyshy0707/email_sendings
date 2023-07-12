FROM python:2.7.18-alpine
RUN apk update && apk add python2-dev gcc libc-dev
RUN apk add nano
RUN apk add -U tzdata
RUN export LC_ALL=ru_RU.UTF-8
RUN export LANG=ru_RU.UTF-8

WORKDIR /code
COPY ./src/ ./src
COPY ./requirements.txt ./src/requirements.txt
COPY ./server-entrypoint.sh ./src/server-entrypoint.sh
COPY ./worker-entrypoint.sh ./src/worker-entrypoint.sh

RUN pip install --upgrade pip==20.3.4
RUN pip install -r ./src/requirements.txt

RUN chmod +x /code/src/server-entrypoint.sh
RUN chmod +x /code/src/worker-entrypoint.sh