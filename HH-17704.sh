curl "http://ashaposhnikov.pyn.ru:8998/vacancy?lang=RU&hh-session=id%28265874%29%2Ctype%28back_office_user%29&id=3337770&site=1" > m1 && curl "dev:9204/vacancy?lang=RU&hh-session=id%28265874%29%2Ctype%28back_office_user%29&id=3337770&site=1" > d1 && diff -p m1 d1

