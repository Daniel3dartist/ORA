import os, sys
import json


class ItemGen:
    def gen():
        path = os.getcwd()
        print(path.replace('\\','/')+'/fake_gen/faker_generator/generators/shop_itens.json')
#        path = path.replace('c:\\', 'c://')
        try:
            path = os.getcwd()
            file = open(path.replace('\\','/')+'/generators/shop_itens.json', 'r')
            j = json.load(file)
            return j
        except:
            return 'ERRO on read shop_itens.json file'