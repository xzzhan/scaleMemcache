#!/bin/bash

for k in {1..8}
do
    ./request.py -i $k &
    
    echo "$k threads has been created on each client server!\n"
    sleep 0.5
done

