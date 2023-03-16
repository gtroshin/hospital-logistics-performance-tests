# Hospital Logistics Performance Tests
![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-green.svg)
![Locust 2.10.1](https://img.shields.io/badge/Locust-2.10.1-purple.svg)

This project is designed to run performance tests using the Locust framework against the services with the following
profile:

Number of users (peak concurrency): 4 \
Spawn rate (users started/second): 10 \
Duration (run time): 3 minutes

All the performance test information is available at the inbuilt [Locust charts](http://localhost:8089) and at
[custom Grafana dashboard](http://localhost:3000/d/0WllLp6mq/locust-test).

Tests output the basic statistics and the results to the console and will exit with `1` status code if there were any
errors or failures in tests.

Grafana's settings, including the data source and a dashboard pre-provisioned.

## Requirements

* Docker
* [Python 3.9.1+](https://www.python.org/downloads/release/python-3910/)

## Development

To start all the services, run the following command in the project root folder:

    docker-compose up -d && docker-compose logs --follow locust

To debug all the logs from services run:

    docker-compose up

For the local test development outside docker environment, install the dependencies:

    pip3 install -r requirements.txt

## Services and addresses

| Service          | Address                       | Description                          |
|------------------|-------------------------------|--------------------------------------|
| Locust           | http://localhost:8089         | Load testing tool                    |
| Exported Metrics | http://localhost:9646/metrics | Locust metrics exporter              |
| Prometheus       | http://localhost:9090         | Data source for Grafana              |
| Grafana          | http://localhost:3000         | Visualization and observability tool |
