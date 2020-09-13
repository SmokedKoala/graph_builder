
import requests
import re
import json
import pydot
from graphviz import Digraph
from graphviz import Source
import os

# были проблемы с PATH, добавил вручную
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz 2.28\\\bin'

package_dict = {}
# функция парсинга JSON
def json_parse(package_name):
    request =requests.get(f'https://pypi.org/pypi/'+package_name+'/json')
    package_dict[package_name]=[]
    # print(request.json()["info"]['requires_dist'])
    # проверка, есть ли необходимые пакеты
    if not request.json()["info"]['requires_dist'] == None:
        # добавление необходимых пакетов в словарь
        for dependence_name in request.json()["info"]['requires_dist']:
            if not re.search(r'extra',dependence_name):
                dependence_name=re.sub('[^a-zA-Z_-]', '', dependence_name)
                package_dict[package_name].append(dependence_name)
        # рекурсивный вызов функции для следующих пакетов
        for name in package_dict[package_name]:
            if not name in package_dict and requests.get(f'https://pypi.org/pypi/'+name+'/json').status_code == 200:
                json_parse(name)
#   функция создания графа   
def graph_creation():
    dot = Digraph()
    for key in package_dict.keys():
        dot.node(key)
        for name in package_dict[key]:
            dot.edge(key,name)
    print(dot.source)
    dot.render()


package_name = str(input()).lower()
json_parse(package_name)
# for _ in package_dict:
    # if package_dict[item_key] == []:
        # package_dict.pop(item_key)
# print(package_dict)
graph_creation()