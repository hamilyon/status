#!/bin/sh
cd /home/ashaposhnikov/re/bleeding_edge/sofea-webapp/
MAVEN_OPTS="-Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,address=4000,server=y,suspend=n ${MAVEN_OPTS}" nice -n 16 mvn-hh jetty:run &
cd /home/ashaposhnikov/re/bleeding_edge/hh-webapp/
MAVEN_OPTS="-Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,address=4001,server=y,suspend=n ${MAVEN_OPTS}" nice -n 16 mvn-hh jetty:run -Dhh.stopPort=8081 -Dhh.stopKey=jjj &
sleep 30
tries=0
while [ $tries -lt 18 ]; do
  curl "localhost:8998/status"
  if [ "${?}" = "0" ]; then
    break
  fi
  sleep 6
done
while [ $tries -lt 10 ]; do
  curl "localhost:8080/status"
  if [ "${?}" = "0" ]; then
    break
  fi
  sleep 2
done
curl "localhost:8998/status"
if [ "${?}" = "0" ]; then
    curl "localhost:8080/status"
    if [ "${?}" = "0" ]; then
      notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'Dev env is up' 'hh-as + sofea'
    else
      notify-send 'Dev env failed to run'
    fi
else
  notify-send 'Dev env failed to run'
fi


