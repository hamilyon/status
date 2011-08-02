#!/bin/sh
cd /home/ashaposhnikov/re/bleeding_edge/hh-webapp/
MAVEN_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,address=4001,server=y,suspend=n ${MAVEN_OPTS}" nice -n 16 mvn-hh jetty:run -Dhh.stopPort=8081 -Dhh.stopKey=jjj &
tries=0
while [ $tries -lt 253 ]; do
  curl "localhost:8080/status"
  if [ "${?}" = "0" ]; then
    break
  fi
  sleep 3
done
curl "localhost:8080/status"
if [ "${?}" = "0" ]; then
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'hh-as is up'
else
    notify-send 'hh-as failed to run'
fi


