# pull official base image
FROM python:3.9-slim-bullseye

# set work directory
WORKDIR /usr/sourcemeter

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install necessary packages
RUN apt-get update \
    && apt-get -y install build-essential \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install netcat \
    && apt-get -y install git

RUN pip install pylint~=2.3.1

COPY . .

RUN chmod +x ./analyze.sh

ENTRYPOINT ["./analyze.sh"]
