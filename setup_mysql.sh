#!/bin/bash 

set -x

sudo apt-get update
sudo docker pull mysql/mysql-server:latest
sudo docker run --name=mysql_docker -d mysql/mysql-server:latest

sudo apt-get install mysql-client
sudo mkdir -p /root/docker/mysql_docker/conf.d

sudo docker kill mysql_docker
docker run \
--detach \
--name=mysql_docker \
--env="MYSQL_ROOT_PASSWORD=[my_password]" \
--publish 6603:3306 \
--volume=/root/docker/[container_name]/conf.d:/etc/mysql/conf.d \
mysql
