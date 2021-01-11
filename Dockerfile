FROM python:3.7-alpine

RUN apk add tiff-dev jpeg-dev zlib-dev freetype-dev lcms2-dev libwebp-dev tcl-dev tk-dev
RUN apk add --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    && rm -rf /var/cache/apk/*

RUN mkdir /app_1
RUN mkdir /static
WORKDIR /app_1

COPY requirements.txt /app_1

RUN pip install --upgrade pip \
    && pip install -r requirements.txt