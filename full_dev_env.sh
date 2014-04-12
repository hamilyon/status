#!/bin/sh
sudo service nginx start
dev_env.sh &
cd ~/re/frontik
python dev_run.py

