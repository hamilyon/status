cd /home/ashaposhnikov/re/bleeding_edge/sofea-webapp/
MAVEN_OPTS="-Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,address=4000,server=y,suspend=n ${MAVEN_OPTS}" nice -n 16 mvn-hh jetty:run &
sleep 30
tries=0
while [ $tries -lt 18 ]; do
  curl "localhost:8998/status"
  if [ "${?}" = "0" ]; then
    break
  fi
  sleep 6
  tries=$((tries+1))
done
curl "localhost:8998/status"
if [ "${?}" = "0" ]; then
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'Sofea is up' 
else
    notify-send 'Sofea failed to run'
fi

