'''=====SEO TOOL TO ANALYSE LIVE WEBPAGES====='''
from urllib.request import urlopen as url         
from bs4 import BeautifulSoup as soup
import re
import matplotlib.pyplot as plt
from collections import Counter




'''***CHECKING URL IS CORRECT OR NOT***'''
url_pattern=re.compile('(http://|https://)www.[a-zA-Z]{3,20}.(com|org|in|co.in)')



def geturl(n):

    reading_webpage_html=url(n)
    parsing_webpage_html=soup(reading_webpage_html,'html.parser')
    
    for script in parsing_webpage_html(["script","style"]):
        script.extract()
    
    text=parsing_webpage_html.get_text()
    line=text.split()
    
    f=open('stopwords.txt')
    g=f.readlines()
    stopwords=[word.strip() for word in g]
    
    final=[]
    for i in line:
        if i not in stopwords:
            final.append(i)
    
    strfinal=str(final)
    l=[]
    for i in final:
        if i not in l:
            l.append(strfinal.count(i))
    more=max(l)   
    maximum=more/2 
    
    d={}
    for i in final: 
       c=strfinal.count(i)
       if c>maximum:
         d[i]=c
         
    j=Counter(d)
    print(j)
    
    
    plt.bar(range(len(d)), d.values(), align='center')
    plt.xticks(range(len(d)), d.keys())
    plt.show()

file=open('url.txt')
lines=file.readlines()
l=[]
for i in lines:
    for w in i.split():
       # print(w)
        l.append(w)
for i in l:
    print(i)
    geturl(i)
    
