FROM brunneis/python:3.7
RUN apt-get update && apt-get -y install wget build-essential libssl-dev zlib1g-dev
ADD easyaerospike.tar /
WORKDIR easyaerospike
RUN pip install -r requirements.txt && python setup.py install
