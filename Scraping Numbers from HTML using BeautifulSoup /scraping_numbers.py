from urllib import request
from bs4 import BeautifulSoup


html = request.urlopen('http://py4e-data.dr-chuck.net/comments_2013947.html').read()

soup = BeautifulSoup(html, 'lxml')

tags = soup('span')

soma = 0

for tag in tags:
    soma += int(tag.contents[0])
print(soma)