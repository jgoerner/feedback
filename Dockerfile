###################################################
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

## --- MISC --- ##
# Update apt Cache
RUN apt-get update -y
# Install required programms
RUN apt-get install -y \
python2.7 \
python-pip \
postgresql-9.5 \
postgresql-server-dev-9.5 \
vim \
git \
nano

## ---  PYTHON --- ##
# Put python requirements file into container
ADD ./installation_settings/requirements.txt /tmp/requirements.txt
# Update PIP & install required python modules
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
# Create aliase for convenience
RUN alias python="python2.7"
# Route port 8080 (web.py) to host
EXPOSE 8080

## --- POSTGRES --- ##
# put postgres installation file into container
ADD ./installation_settings/create_database.sql /tmp/create_database.sql
# Postgres:	su postgres && /etc/init.d/postgresql start && psql

## --- JUPYTER --- ##
# put jupyter config into container
ADD ./installation_settings/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
# Route port 8888 outside container for development
EXPOSE 8888

## --- SOURCE CODE --- ##
WORKDIR /opt/jestherday/
ADD ./ ./
