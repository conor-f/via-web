# Via

<img src="/assets/logo.png" alt="via logo" style="height: 100px; width:100px;"/>

Road quality assessment from cycling / driving / bussing around, tools to analyse data collected from the android app https://github.com/RobertLucey/road-quality-aggregator

All uploaded data is public and no accounts required. Neat privacy to make it very difficult / impossible (depending on your settings and how many trips have been taken in the area) to find the route of an individual journey as well as its origin / destination

## Usage

To get things going:
 1. Run `make run`
 2. Open http://localhost:8080

### Docker

A web interface has been Dockerized and is available [here](https://hub.docker.com/repository/docker/conorjf/via-web).
The easiest way to run locally is to use the available `docker-compose` file.
Note that you will need some AWS credentials to pass to this. These should be
placed in a `.env` file in the same working directory as `docker-compose.yaml`
as follows:

```
AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXXXX
```
