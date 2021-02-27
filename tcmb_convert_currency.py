print("merhaba dolar")
print("merhaba euro")


# tcmb sitesinden efektif dolar satış fiyatını çekelim
# https://www.turkiye.gov.tr/doviz-kurlari

from bs4 import *
import requests

sayfa = requests.get("https://www.turkiye.gov.tr/doviz-kurlari")
# bu code başarılıysa 200 kodunu döner.
#print(sayfa)

#bu kod sayfa kaynağını çıkarır
# print(sayfa.text)

soup = BeautifulSoup(sayfa.text, "html.parser")

effective_sell_dolar = soup.find("td", text="1 ABD DOLARI").text
print(effective_sell_dolar)
#kodu böleceksem \ koymalıyım
#fonksiyonun içini direkt aşağı atabilirim.
#     .find_next_sibling("td") şeklinde de yazılabilir, input vermeden de çalışıyor.
effective_sell_dolar_1 = soup.find("td",
                                   text="1 ABD DOLARI")\
    .find_next_sibling()\
    .find_next_sibling()\
    .find_next_sibling()\
    .find_next_sibling().text\

print(effective_sell_dolar_1)