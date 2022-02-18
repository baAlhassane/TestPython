from random import randint
import requests
from bs4 import BeautifulSoup
import gzip



def http_request(url):
    #url="https://httpbin.org/anything"
    response=requests.get(url)
    soup=BeautifulSoup(response.text)
    return soup




class FileProducts:
      def readFile(self,filename):
         with gzip.open(filename, 'rb') as f:
             file_content = str(f.read())
             print(file_content)
             
             
              
    
    
    
    
if __name__ == "__main__":
    url="https://httpbin.org/anything"
    #print(h ttp_request(url))
    file=FileProducts()
    file.readFile("C:\\Users\\DVEEC\\alhas\\python\\testpyton\\third_part\\data\\data.json.gz")