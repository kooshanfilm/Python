import requests

url = "https://www.vfsvisaonline.com/Netherlands-Global-Online-Tracking_Zone3/Track.aspx"

querystring = {"P":"XAvtfj4b1oOCybpMtuO+Ig%3d%3d"}

payload = "__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=fJZuKOxvFdGYgib%252FNQ9Y7WkvzkBJ4YeP8Yl92XpGmEdB5CO7DHqO5mL4Nrpxsrv7%252Fa9LuacBtdCGnsP8R0yQZvdmSZYGcUe9CV24o%252BtFGCGN2TfDmW3LjeEKdNOumY383p%252Br8L4oXUfHfWvNNwl%252BQaALyLMz4UWFA4beY4UsOwoHwndRnE%252B26NnBnERR4jBvHAjbMhme1Jp47enTX74nKA9PIYTw42NenyyhWHQVPTkPHnOM&__VIEWSTATEGENERATOR=75CAD07E&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=jj9NsuJiiur1O9iSLmCqtG%252FEijIsxKC0mPD%252FamATmTlMeKZ0Rp4ySkdzFUW%252BaC0LjwSHKbWd6lSyw8Sj1N2GOXa1y8nVJckL3JswbhiMDC74vx6Lf%252BQKNsLdoh0JE8GoCJLBQVfdb0WURSYj3P9lq0QFgxMy7rmrsxtDH6hpfR7qbjPC&ctl00%2524plhMain%2524txtTrackingNo=van290057957&ctl00%2524plhMain%2524btnSubmit=Submit"
headers = {
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Origin': "https://www.vfsvisaonline.com",
    'Upgrade-Insecure-Requests': "1",
    'DNT': "1",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Referer': "https://www.vfsvisaonline.com/Netherlands-Global-Online-Tracking_Zone3/Status.aspx?P=XAvtfj4b1oOCybpMtuO+Ig%3d%3d",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9,fa;q=0.8",
    'Cookie': "ASP.NET_SessionId=q3ijqv4eg1o1kf0xzime05cl",
    'Postman-Token': "a5802ca1-2d02-c7cc-e476-7c6e6cb94be7"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)