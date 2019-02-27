#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

"""
Python syslog client.

This code is placed in the public domain by the author.
Written by Christian Stigen Larsen.

https://www.netkiller.cn/python/library/syslog.html

See RFC3164 for more info -- http://tools.ietf.org/html/rfc3164

Note that if you intend to send messages to remote servers, their
syslogd must be started with -r to allow to receive UDP from
the network.
"""

import socket


FACILITY = {
	'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
	'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
	'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
	'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
	'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23,
}

LEVEL = {
	'emerg': 0, 'alert':1, 'crit': 2, 'err': 3,
	'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
}

def syslog(message, level=LEVEL['notice'], facility=FACILITY['daemon'],
	host='localhost', port=514, source='localhost'):

	"""
	Send syslog UDP packet to given host and port.
	"""

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((source, 0))
	data = '<%d>%s' % (level + facility*8, message)
	sock.sendto(data, (host, port))
	sock.close()


import argparse
parser = argparse.ArgumentParser(description='Send syslog from pseudo-device')
parser.add_argument('id', type=int, help='device number [1..6000+]')

def main():
	sec1 = "10.51.170.28" #  .26 = direct, .28 = shared
	sec2 = "10.117.148.14"

	args = parser.parse_args()
	id = args.id

	src = "%s%i" % (
		"COR" if id <= 3000 else "MSS",
		(224+id)
	)
	dest_ip = sec1 if id <= 3000 else sec2
	src_ip = "192.168.%i.%i" % ( id / 256, id % 256 )

	text = fortinet_syslog(src, id)
	syslog(message=text, level=6, facility=5, host=dest_ip, source=src_ip)


import datetime

def basic_syslog(src, id):
	return "%s: pseudo-syslog from SIM-1:%i" % (src, id)

def fortinet_syslog(src, id):
	now = datetime.datetime.now()
	return "date=%s time=%s devname=%s devid=FG-pseudo-%i type=event level=info" % (
		now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), src, id)



if __name__ == "__main__":
	main()
