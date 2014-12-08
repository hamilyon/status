#!/bin/sh
sudo service nginx start
dev_env.sh &
cd ~/re/hh.sites.main/
python dev_run.py &
cd ~/re/logic
python dev_run.py &

