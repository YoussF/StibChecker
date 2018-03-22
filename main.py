#!/usr/bin/python2
import urllib
import os
from xml.etree import ElementTree
from time import sleep

ligne = raw_input("Ligne : ")
sense = raw_input("Sense : ")
while True:
	os.system('tput reset')
	url = urllib.urlopen('http://m.stib.be/api/getitinerary.php?line={}&iti={}'.format(ligne, sense))
	feed = ElementTree.parse(url)
	for stop in feed.findall('stop'):
		if stop.findtext('present'):
			print '[x] '+stop.findtext('name')
		else:
			print '[ ] '+stop.findtext('name')

	sleep(10)
