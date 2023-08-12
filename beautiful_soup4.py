import requests
from bs4 import BeautifulSoup

url = '''https://www.futhead.com/23/players/'''
data = requests.get(url)
html = data.content
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
data = soup.find_all('span',{'class':'player-name'})
# print(data)
data_name = []
for i in data:
     data_name.append(i.string)
# print(data_name)

data = soup.find_all("span",{'class':'revision-gradient'})
# print(data)
data_rating = []
for i in data:
     data_rating.append(i.string)
# print(data_rating)

temp = []
final_data = []
count =0
while count<10:
     temp.append(data_name[count])
     temp.append(data_rating[count])
     final_data.append(temp)
     temp=[]
     count+=1
print(final_data)
for i in final_data:
     print(i)
     # print("\n")