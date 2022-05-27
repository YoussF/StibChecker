"""File that scrap the STIB's website in order to get information about a line."""
import urllib
import os
from xml.etree import ElementTree
from time import sleep
import urllib.request

line = input("Line : ")
direction = input("Direction : ")

while True:
	os.system('tput reset')
	url = urllib.request.urlopen(f"http://m.stib.be/api/getitinerary.php?line={line}&iti={direction}")
	feed = ElementTree.parse(url)
	for stop in feed.findall('stop'):
		if stop.findtext('present'):
			print(f"[x] {stop.findtext('name')}")
		else:
			print(f"[ ] {stop.findtext('name')}")
	sleep(10)
