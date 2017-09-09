#!/usr/bin/python

import pycurl
import json
import urllib2

#The IP Address of your Hue Bridge
HUE_BRIDGE = ""
#The group IDs of the light groups you wish to toggle on/off
HUE_GROUP_IDS = []
#Your Hue Bridge user ID
API_KEY = ""

c = pycurl.Curl()
c.setopt(pycurl.CUSTOMREQUEST, "PUT")

def toggleGroupState():
	light_states = {}
	for id in HUE_GROUP_IDS:
		url = 'http://' + HUE_BRIDGE + "/api/" + API_KEY + "/groups/" + str(id)
		data = json.load(urllib2.urlopen(url))
		c.setopt(pycurl.URL, url + "/action")
		
		if(data["state"]["all_on"]):
			c.setopt(c.POSTFIELDS, "{\"on\":false}")
		else:
			c.setopt(c.POSTFIELDS, "{\"on\":true}")		
		c.perform()
