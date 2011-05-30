#!/bin/sh
cd /home/ashaposhnikov/re/bleeding_edge/sofea-webapp/
MAVEN_OPTS="-Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,address=4000,server=y,suspend=n ${MAVEN_OPTS}" nice -n 16 mvn-hh jetty:run &
cd /home/ashaposhnikov/re/bleeding_edge/hh-webapp/
MAVEN_OPTS="-Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,address=4001,server=y,suspend=n ${MAVEN_OPTS}" nice -n 16 mvn-hh jetty:run -Dhh.stopPort=8081 -Dhh.stopKey=jjj &
