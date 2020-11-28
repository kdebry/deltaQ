FROM python:3.8.5-alpine3.12

WORKDIR /app

COPY . /app

RUN apk update && apk add libc-dev
RUN apk add build-base
RUN apk --no-cache add curl

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["run.py"]
