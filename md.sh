MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=128m" nice -n 16  mvn-hh clean install org.apache.maven.plugins:maven-eclipse-plugin:2.9:eclipse -DdownloadSources=true -ff -T8 -U
if [ "$?" = "0" ]; then 
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'Build finished'
else
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/css/ambient/blocks/form/error/triangle.png 'Build faliled miserably'
    exit 1
fi
