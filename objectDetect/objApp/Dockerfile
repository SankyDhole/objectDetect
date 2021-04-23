FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /objectdetector

COPY requirements.txt /objectdetector/

RUN pip install -r requirements.txt

COPY . /objectdetector/