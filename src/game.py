from src.confloader import *
from src.character import *
from src.alchemist import *

#游戏本体

class Game:
    #用于储存游戏本体数据内容，其余活动不保存在此处，只进行注册
    def __init__(self, *savenames):
        #savename为存档名称
        for save in savenames:
            self.save = save
        #建立新存档
        self.conf = Configures()
        self.gold = 5000 #金币
        self.time = 0 #时间
        self.maincharacter = Character() #主人物，玩家控制
        self.items = [{'id':10000001,'num':10}, {'id':10000002,'num':10}, {'id':10000003,'num':10}] #字典{id:个数}
        
    #游戏基础逻辑：处理事务太麻烦，不做类封装了
    
    #休息一回合，回复一半的体力值
    def game_Rest(self):
        self.time += 1
        self.maincharacter.vigor += int(self.maincharacter.vigor_max/2)
        if(self.maincharacter.vigor > self.maincharacter.vigor_max):
            self.maincharacter.vigor = self.maincharacter.vigor_max
        return True

    #开始炼金
    def game_StartAlchemy(self):
        #self.alchemy = Alchemy()
        
        if(self.maincharacter.vigor - 1 < 0):
            return False
        else:
            self.time += 1
            self.maincharacter.vigor -= 1
            return True