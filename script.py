import requests, time

url = "http://172.16.60.170:8080"
for i in range(15):
	#get url
	time.sleep(2)
	r = requests.get(url)
	print(r.text)
	print('--------------------------------', end="\n")
