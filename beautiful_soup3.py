import requests
from bs4 import BeautifulSoup

url = '''https://www.thetimenow.com/india'''
data = requests.get(url)
html = data.content
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
time = soup.find_all('span',{'id':'main_time'})
time_string = time[0].string
print(time_string)