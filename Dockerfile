# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /code


RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev build-base libffi-dev openssl-dev
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/
