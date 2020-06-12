FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
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
#
#CMD [ "./manage.py","runserver","0.0.0.0:8000" ]
