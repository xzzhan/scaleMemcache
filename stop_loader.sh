#!/bin/bash

ssh thermalcam@128.148.16.115 'pkill -f "run_loader.py"' 
ssh xinzhan@128.148.16.126 'pkill -f "run_loader.py"' 
#ssh scale@128.148.16.168 'pkill -f "run_loader.py"'
pkill -f "run_loader.py"

