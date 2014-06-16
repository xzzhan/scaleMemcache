#!/bin/bash

freq=("1600" "1867" "2267")
name="exp"

./run_loader.py -n 4 -t 18100


for i in 0 1 2
do
	temp_freq=${freq[$i]}
	ssh scale@128.148.16.164 ./masterfreq$temp_freq
	ssh scale@128.148.16.165 ./masterfreq$temp_freq
	ssh scale@128.148.16.178 ./masterfreq$temp_freq
        
        echo "Start to measure the utilizations\n"
	./run_loader.py -n 4 -t 60 &
	./py_memcached/monitor_memcache.py &
	./get_utilization 

        
	pkill -SIGTERM -f "run_loader.py"
	pkill -f "monitor_memcache.py" 
        ./stop_loader.sh
	echo "Simulation $i terminated!\n"
	mv server* ./temp_name
        mv delay* ./temp_name
	mv temp_name ../$name$i

        sleep 10
done

