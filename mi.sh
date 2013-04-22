grep -l maven.pomderived  .classpath */.classpath 2>&1 1>/dev/null
if [ "$?" = "0" -o "$?" = "2" ]; then
    echo "To avoid possible coflict with m2eclipse skipping maven eclipse plugin target. Delete .classpath files manually to do full rebuild"
    nice -n 16  mvn-hh clean install -ff -T8
else
    nice -n 16  mvn-hh clean install org.apache.maven.plugins:maven-eclipse-plugin:2.9:eclipse -ff -T8
fi

if [ "$?" = "0" ]; then 
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'Build finished'
else
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/css/ambient/blocks/form/error/triangle.png 'Build faliled miserably'
    exit 1
fi
