#!/bin/bash

[ "$1" ] || { echo "usage: $0 <device id>"; exit 0; }

while true; do
	./syslog.py $1
done
