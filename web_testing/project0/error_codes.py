import requests

url = 'http://httpbin.org/html'
req = requests.get(url)
print ("response code:",req.status_code)
