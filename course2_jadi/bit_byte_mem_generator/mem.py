import sys
import requests
from bs4 import BeautifulSoup

word = "rabbit"
url = 'https://www.google.com/search?sca_esv=599466310&sxsrf=ACQVn09CjnPbZd5imNEzpzCcUQc7AEStmQ:1705588648300&q=%s&tbm=isch&source=lnms&sa=X&ved=2ahUKEwj3xI7slOeDAxXT_rsIHbJqBtYQ0pQJegQIDxAB&biw=1280&bih=639&dpr=1.5' % word

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

try:
  print(soup.find_all("img")[2]['src'])
except:
  print("")