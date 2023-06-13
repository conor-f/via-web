FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /code

RUN apt -y update
RUN apt -y install make build-essential npm vim

COPY . .

EXPOSE 8080

CMD ["make", "production_run"]
