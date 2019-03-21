from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
file=open('census.csv','w')
file.write('ID\n1')
file.close()
df=pd.read_csv('census.csv')
df['CITY']=None
df['POPULATION']=None
df['STATE']=None
url="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
try:
	result=urllib.request.urlopen(url)
except urllib.error.URLError as en:
	print('Connection Error...')
	exit(0)
c=result.read()
soup=BeautifulSoup(c)
div=soup.find('div',{'id':'mw-content-text','class':'mw-content-ltr'})
ind=div.find('div',{'class':'mw-parser-output'})
table=ind.find_all('table',{'class':'wikitable sortable'})
count=0
sol=[]
for area in table:
	temp1=area.find('tbody')
	temp=temp1.find_all('tr')
	flag=0
	for i in temp:
		if flag==0:
			flag+=1
			continue
		id=i.find_next('td')
		df.set_value(count,'ID',count+1)
		city=id.find_next('td')
		city1=city.find_next('a').contents[0]
		df.set_value(count,'CITY',city1)
		pop=city.find_next('td')
		pop1=int(pop.contents[0].replace(',',''))
		df.set_value(count,'POPULATION',pop1)
		state=pop.find_next('td').find_next('td')
		df.set_value(count,'STATE',state.find_next('a').contents[0])
		if pop1>500000:
			sol.append(city1)
		count+=1
df.to_csv('census.csv',index=False)
print('Cities having population greater than 5lakhs are as follows:')
for i in sol:
	print(i)