import requests

from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/humanscale-liberty-office-chair/black/p839103")
content = request.content
soup = BeautifulSoup(content,"html.parser")
elemnt = soup.find("p",{"class":"u-centred price"})
string_price = elemnt.text

price_without_symbole = string_price[1:]
print(float(price_without_symbole))

#class="u-centred price"