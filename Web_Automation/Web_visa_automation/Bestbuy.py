import requests

from bs4 import BeautifulSoup

request = requests.get("https://www.bestbuy.ca/en-ca/product/beats-by-dr-dre-beats-by-dr-dre-solo3-on-ear-sound-isolating-bluetooth-headphones-gold-mner2ll-a/10488058")
# content = request.content
# soup = BeautifulSoup(content,"html.parser")
print request
# elemnt = soup.find("p",{"class":"u-centred price"})
# string_price = elemnt.text

# price_without_symbole = string_price[1:]
# final_price = (float(price_without_symbole))
# print (final_price)


                                                        
                                                   