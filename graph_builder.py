import requests
from bs4 import BeautifulSoup

def package_dowload():
    package_name = str(input())
    page = requests.get("https://pypi.org/simple/"+package_name)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find_all('a')
    # link = results[-2].get('href')
    # print(link)
    
    file = open("current_pip_package.rar", "wb")
    ufr = requests.get(results[-2].get('href'))
    file.write(ufr.content)
    file.close



package_dowload()