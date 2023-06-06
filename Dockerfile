FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /code

RUN apt -y update && apt -y install make build-essential python-numpy python-setuptools python3-scipy libatlas-base-dev libatlas3-base python3-pip npm vim

RUN python3 -m pip install virtualenv
RUN python3 -m virtualenv -p python3 .env_python3

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

RUN make production_setup

EXPOSE 8080

CMD ["make", "production_run"]
