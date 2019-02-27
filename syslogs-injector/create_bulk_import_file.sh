#!/bin/bash

PROG=$(basename "$0")

case $1 in
	""|-h)
		echo "usage: $PROG <nb devices>"
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


	echo "OPERATOR_PREFIX,CUSTOMER_ID,DEVICE_NAME,WORK_ORDER_REFERENCE,
		SITE_ADDR_STREETNAME1,
		SITE_ADDR_STREETNAME2,
		SITE_ADDR_STREETNAME3,SITE_ADDR_ZIPCODE,SITE_ADDR_CITY,SITE_ADDR_COUNTRY,
		DEVICE_LOGIN,DEVICE_PASSWORD,DEVICE_ADMIN_PASSWORD,
		WAN_IP,WAN_MASK,WAN_ITF_NAME,HOSTNAME,SERIAL_NUMBER,DEVICE_USE_AUTOMATIC_UPDATE,
		MANUFACTURER_ID,MODEL_ID,CONFIGURATION_VARIABLES
	" | tr -d '\n\t'
	echo

for i in `seq ${nb_itf}`; do
	ip_addr=$( printf "192.168.%i.%i\n" $((i/256)) $((i%256)) )

	echo "op1,8,Linux-${i},Equipment_${i},
		Merchant's House,
		Love Lane Industrial Estate Cirencester,
		Gloucestershire,GL7 1YG,Cirencester,UK,
		usertest,usertestpwd,usertestpwd,
		${ip_addr},255.255.0.0,
		Vlan1,RouterUBQ-${i},,FALSE,
		14020601,14020601,PORT_LINE=2002|PPP_HOS NAME=AYEGRHZ
	" | tr -d '\t\n'
	echo
done
