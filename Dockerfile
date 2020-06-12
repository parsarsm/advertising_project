FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow


COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/








#FROM python:3.8.0-alpine
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#WORKDIR /my-django-app
#
##RUN rm -rf /var/cache/apk/* && \
##    rm -rf /tmp/*
##RUN apk update
#
#
#ADD ./requirements.txt .
##RUN pip install -r requirements.txt
#RUN pip install django djangorestframework Pillow django-nose coverage
#
#
#ADD ./ ./
#K
CMD [ "./manage.py","runserver","0.0.0.0:8000" ]
