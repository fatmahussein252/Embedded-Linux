import requests

#get the ip ({"ip":"41.42.227.148"})
ip=requests.get('https://api.ipify.org/?format=json').text
print(ip)

#extract the ip part of the string (41.42.227.148) 
ip=ip[7:20]
print(ip)

#get location using ip
url='https://ipinfo.io/'+ ip +'/geo'
print(requests.get(url).text)
