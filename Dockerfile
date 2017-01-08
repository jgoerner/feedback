####################################################
# This Dockerfile contains the 'recipe' for        #
# the Docker container used to run the source code #
#						   #
# Author: Joshua Goerner			   #
#	  joshua.goerner[at]jestherday[dot]com	   #
#						   #
####################################################
# for more information about docker, see:          #
# http://www.docker.com				   #
####################################################

# Build on top of current LTS ubuntu
FROM ubuntu:latest

# Update apt Cache
RUN apt-get update -y

# Install required programms
RUN apt-get install -y \
python2.7 \
python-pip \
postgresql

# Create aliase for convenience
RUN alias python="python2.7"

# Create project space & change current dir
ADD ./test /opt/webapp
WORKDIR /opt/webapp

# Commandos to run the installed software
# Python:	python2.7 or python
# Postgres:	su postgres && /etc/init.d/postgresql start && psql
