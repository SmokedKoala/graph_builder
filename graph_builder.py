import requests
import re
import os
import shutil
import zipfile
from bs4 import BeautifulSoup

def package_dowload():
    page = requests.get("https://pypi.org/simple/"+package_name)
    soup = BeautifulSoup(page.text, "html.parser")
    results = soup.find_all('a')
    # link = results[-2].get('href')
    # print(link)
    file = open("current_pip_package.zip", "wb")
    file_reference = requests.get(results[-2].get('href'))
    file.write(file_reference.content)
    file.close
    with zipfile.ZipFile("current_pip_package.zip", "r") as zip_folder:
        zip_folder.extractall("current_pip_package")
    # shutil.rmtree(os.getcwd()+"/current_pip_package.zip")



def unpacking():
    tree = os.walk("current_pip_package")
    # print(tree[-1][0])
    for i in tree:
        # if len(re.findall(REGEX,i,re.MULTILINE))>0:
        print(i)   
    
package_name = str(input()).lower()
# REGEX = package_name[0].upper()+package_name[1:]+".dist-info\METADATA"
package_dowload()
unpacking()