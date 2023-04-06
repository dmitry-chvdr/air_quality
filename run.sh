#!/bin/bash
docker build . -t aqi_image
docker container run --name aqi -d -p 8000:8000 aqi_image