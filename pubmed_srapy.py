from bs4 import BeautifulSoup
import requests
import time
import pickle

urls=['http://www.medlive.cn/pubmed/pubmed_search.do?q=antineoplastic+drugs&page={}'.format(str(i)) for i in range(1,100)]
def get_attractions(url,data=None):
     wb_data=requests.get(url)
     pubmed_text=open("C:\\Users\\xiaoy\\Desktop\\1.txt",'wb')
     soup=BeautifulSoup(wb_data.text,'lxml')
     titles=soup.select("div.info > h3 > a")       
     writerss=soup.select('div.info > p > span.gray')
     dates=soup.select('#div_data > div > div > p:nth-of-type(1) > span:nth-of-type(2)')
     for title,writers,date in zip(titles,writerss,dates):
         data={
            'title':list(title.stripped_strings),
            'writers':list(writers.stripped_strings), 
            'date':list(date.stripped_strings)
            }
         
         pickle.dump(data,pubmed_text)

            
         
         
         
      #div_data > div:nth-child(1) > div > p:nth-child(2) > span:nth-child(2)
      #div_data > div > div > p:nth-of-type(2) > span:nth-of-type(2)
      #div_data > div:nth-child(2) > div > p:nth-child(2) > span:nth-child(2)
      #div_data > div:nth-child(3) > div > p:nth-child(2) > span:nth-child(2)  
      
   
'''
def get_favs(url,data=None):

  wb_data=requests.get(url_saves,headers=headers)
  soup=BeautifulSoup(wb_data.text,'lxml')
  titles=soup.select('h2.desc > a[target="blank"]')
  imgs=soup.select('img[width="188"]')                
  cates=soup.select('div.item-price > span')
  print(titles)
  for title,image,cate in zip(titles,imgs,cates):
    data={
        'title':title.get_text(),                                                                                                                                                                                                       
        'image':image.get('src'),
        'cate':cate.get_text()
            }
    print(data)
get_favs(url_saves)'''
page=0
'''with open("C:\\Users\\xiaoy\\Desktop\\1.txt","w")as text:
   text.write("")
   text.close()'''
for url in urls:
   get_attractions(url)
   time.sleep(5)
   print("\n\n")
pubmed_text.close()
   
   

