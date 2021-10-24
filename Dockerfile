FROM ubuntu:20.04

WORKDIR /code

RUN apt -y update && apt -y install build-essential python-numpy python-setuptools python3-scipy libatlas-base-dev libatlas3-base python3-pip

RUN python3 -m pip install virtualenv

COPY . .
RUN make setup

EXPOSE 8080

CMD ["make", "production_run"]
