#!/usr/bin/python

from scapy.all import *
import time
import light

#Your Amazon Dash Button MAC Address
DASH_MAC = '74:75:48:aa:aa:fb'

#Period during which to ignore subsequent BOOTP packets. 
#Sometimes the Dash button will send multiple BOOTP requests, which can cause your action to be triggered multiple times.
RE_PRESS_WINDOW_SEC = 10

last_seen_time = 0

def check_src_mac(pkt):
    global last_seen_time
    global RE_PRESS_WINDOW_SEC
    if(pkt.src == DASH_MAC and time.time() > (last_seen_time + RE_PRESS_WINDOW_SEC)):
        last_seen_time = time.time()
	if(pkt.src == DASH_MAC):
        	light.toggleGroupState()

sniff(filter="udp", prn=check_src_mac, store=0)