import json
import csv
#用于预加载各种游戏参数与对应表

class Configures:
    def __init__(self):
        with open("./conf/Item.csv",'r',encoding="utf-8") as f:
            reader = csv.reader(f)
            fieldnames = next(reader)
            dictreader = csv.DictReader(f,fieldnames=fieldnames)
            self.ItemDict = dict()
            for row in dictreader:
                self.ItemDict[int(row['id'])] = row
            print("Item read finished")

        