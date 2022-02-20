import scrapy

import requests
from  bs4 import   BeautifulSoup 
import lxml

import csv

import urllib.request, urllib.parse, urllib.error

import ssl


'''
class TestScrapy(scrapy.Spider):
    name="alhas"
    url= ["https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"]
    def parse(self,response):
        products=response.css("div._ngcontent-serverapp-c220")
        for product in products:
            print(product)
            
'''    

#%%%%%%%%%%%%%%%%%%%%%%%%%% test de liens qui marches %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""        
#url="https://fr.wikipedia.org/wiki/Portail:Accueil" #wikipedia
url="https://www.yves-rocher.fr/" #yver rocher
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0 ; Win64 ; x64) AppleWebKit/537.36 (KHTML, comme Gecko) Chrome/98.0.4758.102 Safari/537.36"}

response=requests.get(url,headers=headers)        
soup=BeautifulSoup(response.text,'lxml')
mydivs =soup.findAll('div') #,class_='shelfProductTile tile has-header' )
print(mydivs)
print(len(mydivs))
"""

#%%%%%%%%%%%%%%%%%%%%%%%%%% Fin de test de liens qui marches %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




url= "https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0 ; Win64 ; x64) AppleWebKit/537.36 (KHTML, comme Gecko) Chrome/98.0.4758.102 Safari/537.36"
        #"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}


response=requests.get(url,headers=headers)
print(response.text)          
soup=BeautifulSoup(response.text,'lxml')
#mydivs =soup.findAll('section' ,class_='shelfProductTile tile has-header' )
products_div =soup.findAll('div',class_="ng-tns-c233-131 product-grid--tile ng-star-inserted" )
products_share=soup.findAll('shared-product-tile',class_="ng-star-inserted" )
# The description of our products are in thes tags.
print(products_div)
print(len(products_div))



descriptions=[] # the list of the product description
prices=[]# liste of prices 


for product_description in products_div:
    a=product_description.find("a",class_="shelfProductTile-descriptionLink" )
    description=str(a["href"]).split("/")[-1] #href="/shop/productdetails/305224/lipton-ice-tea-peach"
    price=product_description.find("span",class_="price-dollars")
    descriptions.append(description)
    prices.append(price)
    
    
# Write in a file 
file = open("info.txt", "w")
writer = csv.writer(file)

nb=len(prices)
for i in range(nb):
    #iterate through integers 0-nb
    writer.writerow([description[i], prices[i]])

file.close()
    

# this code test the code of write in a file word.
list_1 = ["Hello", "World", "Monty", "Python"]
list_2 = [1, 2, 3, 4]


file = open("columns.csv", "w",  newline='') 
writer = csv.writer(file)
headers_=["name", "price($)"]
writer.writerow(headers_)
for w in range(4): 
    #iterate through integers 0-3
    writer.writerow([list_1[w], list_2[w]])

file.close()

    
 