#!/bin/bash

for i in {1..8}
do
    ssh thermalcam@128.148.16.115 ./request_gen.py &
    ssh xinzhan@128.148.16.126 ./request_gen.py &
    ssh scale@128.148.16.168 ./request_gen.py &	
    ./request_gen.py &
   
    echo "$i threads has been created on each client server!\n"
    sleep 1
done

echo "Start to measure the utilizations\n"
./py_memcached/monitor_memcache.py &
./get_utilization 

echo "Measurements finished!\n"
cp server* ./temp_name
./stop_loader.sh 
pkill -f "monitor_memcache.py" 
echo "Load generator terminated!\n"
