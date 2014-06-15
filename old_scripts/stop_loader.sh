#!/bin/bash

ssh thermalcam@128.148.16.115 'pkill -f "request_gen.py"' 
ssh xinzhan@128.148.16.126 'pkill -f "request_gen.py"' 
ssh scale@128.148.16.168 'pkill -f "request_gen.py"'
pkill -f "request_gen.py"

