FROM python:3.9-alpine3.18
ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

RUN apk update && apk add build-base && apk add bash

ADD ./requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
