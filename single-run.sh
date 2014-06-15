#!/bin/bash


	./run_loader.sh
	pkill -SIGTERM -f "run_loader.sh"
	./stop_loader.sh
	echo "Simulation $i terminated!\n"
	./cleanup.sh

freq=("1600" "1733" "1867" "2000" "2133" "2267")
name="exp"

for i in 0 1 2 3 4 5
do
	temp_freq=${freq[$i]}
	ssh scale@128.148.16.164 ./masterfreq$temp_freq
	ssh scale@128.148.16.165 ./masterfreq$temp_freq
	ssh scale@128.148.16.178 ./masterfreq$temp_freq
#	ssh scale@128.148.16.164 ./masterfreq2267
#	ssh scale@128.148.16.165 ./masterfreq2267
#	ssh scale@128.148.16.178 ./masterfreq1600

	./run_loader.sh
	pkill -SIGTERM -f "run_loader.sh"
	echo "Simulation $i terminated!\n"
	mv server* ./temp_name
	mv temp_name $name$i

done

	ssh scale@128.148.16.164 ./masterfreq1600
	ssh scale@128.148.16.165 ./masterfreq2267
	ssh scale@128.148.16.178 ./masterfreq1600

	./run_loader.sh
	pkill -SIGTERM -f "run_loader.sh"
	echo "Simulation $i terminated!\n"
	mv server* ./temp_name
	mv temp_name exp6
		
	ssh scale@128.148.16.164 ./masterfreq2267
	ssh scale@128.148.16.165 ./masterfreq1600
	ssh scale@128.148.16.178 ./masterfreq1600
	./run_loader.sh
	pkill -SIGTERM -f "run_loader.sh"
	echo "Simulation $i terminated!\n"
	mv server* ./temp_name
	mv temp_name exp7

        ssh scale@128.148.16.164 ./masterfreq1600
	ssh scale@128.148.16.165 ./masterfreq1600
	ssh scale@128.148.16.178 ./masterfreq1600
	./run_loader.sh
	pkill -SIGTERM -f "run_loader.sh"
	echo "Simulation $i terminated!\n"
	mv server* ./temp_name
	mv temp_name exp8


