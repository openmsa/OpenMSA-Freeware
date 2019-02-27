#!/bin/bash

PROG=$(basename "$0")

case $1 in
	""|-h)
		echo "usage: $PROG <nb interfaces>"
		exit 0
		;;
	[0-9]*)
		nb_itf=$1
		;;
	*)
		echo "unknown command: $1"
		exit 1
		;;
esac

for i in `seq ${nb_itf}`; do
	ip_addr=$( printf "192.168.%i.%i\n" $((i/256)) $((i%256)) )
	ifconfig ens256:$i $ip_addr/16 up
done
