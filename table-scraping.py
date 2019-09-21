import numpy as np
import pandas as pd
import requests, bs4

#Get data from the website url
url="https://www.hubertiming.com/results/2017GPTR10K"
req=requests.get(url)
soup=bs4.BeautifulSoup(req.text,"html.parser")

#Get all data in the rows
all_rows=soup.findAll('tr')

#Get table header data
row=all_rows[4]
row1=list(row)
th=list(map(lambda x:(str(x).lstrip('<th>').rstrip('</th>')), row1))
th1=list(filter(lambda x:x!='\n', th))

#Get data from the other rows
row2=[]
td1=[]
td2=[]
for row2 in all_rows[5:]:
    td1=list(map(lambda y:(str(y).lstrip('<td>').rstrip('</td>')), row2))
    td2.append(list(filter(lambda y:y!='\n', td1)))

#Create data frame for further analysis
df=pd.DataFrame(td2, columns=th1)
df.head(20)
