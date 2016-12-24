
from urllib import request
from bs4 import BeautifulSoup
import time
import os

url = input("Enter URL of the Cricket-Match's live score website: ") 

while(True):
	url = request.urlopen(url)
	data = url.read()
	soup = BeautifulSoup(data)
	s = soup.title
	os.system('notify-send -i face-wink "Score" "' + str(s)[7:-41] + '"')
	time.sleep(60)