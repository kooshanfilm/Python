import requests

myheaders = {'user-age':'Iphone 6'}


payload = {'url':'https://staging-manager.eventbase.com'}
#r = requests.get('http://www.httpbin.org/redirect-to',params = payload)
r2 = requests.get('http://www.httpbin.org/headers',headers = myheaders)


print ("Status Code is :",r2.status_code)

for x in r2.headers:
	print (x,r2.headers[x])

print (r2.text)
