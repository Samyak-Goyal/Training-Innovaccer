#!/bin/bash

echo -e "\n$(date "+%T") --- Started\n"
apt-get update
apt-get -y upgrade

apt-get -y autoremove
apt-get autoclean

echo -e "\n$(date "+%T") --- Finished"
