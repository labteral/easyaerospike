#!/bin/bash
tar cf /tmp/easyaerospike.tar ../../
mv /tmp/easyaerospike.tar .
docker build -t easyaerospike .
rm -f easyaerospike.tar
