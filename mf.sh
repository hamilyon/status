mvn-hh clean install -DskipTests -ff -q -T10
if [ "$?" = "0" ]; then 
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'Build finished'
else
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/css/ambient/blocks/form/error/triangle.png 'Build faliled miserably'
    exit 1
fi
