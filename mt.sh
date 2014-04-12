echo $0 $1
mvn-hh test -Dtest=$1
if [ "$?" = "0" ]; then
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/11let/css/hh/blocks/anniversary/logo.png 'Ok'
else
    error_msg=$(cat `find 'target/surefire-reports' -name *$1*txt` | head -8 | tail -3)
    echo $error_msg
    notify-send -i /home/ashaposhnikov/re/bleeding_edge/webapp-static/target/webapp-static/css/ambient/blocks/form/error/triangle.png "$error_msg"
    
    exit 1
fi

