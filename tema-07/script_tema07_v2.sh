#!/bin/bash

cd ~/Desktop/DevOps-CloudBasics/tema-06

python3 main.py

aws s3 sync tweets/ s3://jt-dataeng-giovannagadelha/tema07/tweets/ 
