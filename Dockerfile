FROM python:3.10-slim-bullseye

WORKDIR /code
EXPOSE 8080

COPY . .

CMD ["make", "run"]
