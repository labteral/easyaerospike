#!/bin/bash
docker-compose up -d
python main.py
docker-compose down
