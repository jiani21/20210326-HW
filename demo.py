import requests
from bs4 import BeautifulSoup
req = requests.get("https://csie.asia.edu.tw/project/semester-103")

req.encoding = "utf8" #王經篤big5 #utf8

if req.status_code == 200:
    #print(req.text)
    soup = BeautifulSoup(req.text,"lxml")
    #print(soup)
    
    result1 = soup.find_all("a")
    
    fp = open("out2.txt","w",encoding = "utf8")
    for val in result1:
        text2 = val.text.replace('\n',' ')
        text3 = text2.replace('  ','')
        
        fp.write(text3 + "\n")
        print(text3)
    fp.close()
    #print(result1)

else:
    print("no page")