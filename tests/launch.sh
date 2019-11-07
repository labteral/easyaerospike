#!/bin/bash
docker-compose up -d
sleep 5
python main.py
docker-compose down
