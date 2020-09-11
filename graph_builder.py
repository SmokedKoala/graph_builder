import requests
import re
import os
import shutil
import zipfile
from bs4 import BeautifulSoup

# получение названия пакета с версией из ссылки для скачивания
def full_link(link):
    REGEX = r"\w+[a-zA-Z+-]+[0-9]+[.]+[0-9]+[.]+[0-9]"
    res = re.findall(REGEX, link, re.MULTILINE)
    if len(res) > 0:
        return res[0]
# скачивание пакета, архивирование и разархивирование его в папку
def package_dowload(name_and_version):
    page = requests.get("https://pypi.org/simple/"+package_name)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find_all('a')
    link = results[-2].get('href')
    name_and_version = full_link(link)
    file = open("current_pip_package.zip", "wb")
    file_reference = requests.get(results[-2].get('href'))
    file.write(file_reference.content)
    file.close
    with zipfile.ZipFile("current_pip_package.zip", "r") as zip_folder:
        zip_folder.extract(name_and_version,"current_pip_package")



def unpacking():
    tree = os.walk("current_pip_package")
    for i in tree:
        folder.append(i)
    print(folder)  
    # os.remove("current_pip_package")
    
package_name = str(input()).lower()
folder =[]
name_and_version=""
package_dowload(name_and_version)
# unpacking()