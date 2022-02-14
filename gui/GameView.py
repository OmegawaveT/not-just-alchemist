from cgi import test
from signal import default_int_handler
import sys
import tkinter
from typing import ItemsView
sys.path.append("..")
from src.game import *
#开始游戏后的界面，依附于主界面
class GameView:
    def __init__(self, GameFrame):
        self.GameFrame = GameFrame
        #数据
        self.Game = Game(0)
        self.var_Time = tkinter.IntVar() #时间是有一个换算的，暂时没有设定好
        self.var_Gold = tkinter.IntVar()
        self.var_characterlevel = tkinter.IntVar()
        self.var_charactervigor = tkinter.StringVar()
        self.var_alerttext = tkinter.StringVar()

        #提示框
        self.alerttext = "嗯，一切正常"

        #排版用的框体
        self.pack_rightframe = tkinter.Frame(GameFrame, relief='ridge', borderwidth=2)
        self.pack_rightupframe = tkinter.Frame(self.pack_rightframe, relief='ridge', borderwidth=1)
        self.pack_leftframe = tkinter.Frame(GameFrame)

        self.pack_rightframe.pack(side='right', fill='y')
        self.pack_rightupframe.pack(side='top', fill='x')
        self.pack_leftframe.pack(side='left', fill='both', expand=1)

        #主要框体,除status,home外均用其他类实现
        self.StatusFrame = self.BuildStatusFrame() #常驻
        self.HomeFrame = self.BuildHomeFrame()
        self.AlertFrame = self.BuildAlertFrame()
        self.ItemFrame = False #物品窗口需要在使用时新建，不使用时为false

        self.StatusFrame.pack()
        self.AlertFrame.pack()

        #窗口状态
        self.CurrentFrame = self.HomeFrame
        self.CurrentFrame.pack(fill='both', expand=1)

        

    
    ##状态栏
    def BuildStatusFrame(self):
        StatusFrame = tkinter.Frame(self.pack_rightupframe)
        #固定框
        #StartLine
        tkinter.Label(StatusFrame, text="状态", font=('等线', 16)).pack(side='top')

        StatusFrame_l = tkinter.Frame(StatusFrame)
        StatusFrame_l.pack(side='left')
        #TimeLine
        tkinter.Label(StatusFrame_l, text="时间: ", font=('等线', 10)).pack()
        #GoldLine
        tkinter.Label(StatusFrame_l, text="金币: ", font=('等线', 10)).pack()
        #LevelLine
        tkinter.Label(StatusFrame_l, text="等级: ", font=('等线', 10)).pack()
        #VigorLine
        tkinter.Label(StatusFrame_l, text="精力: ", font=('等线', 10)).pack()

        #变量框
        StatusFrame_r = tkinter.Frame(StatusFrame)
        StatusFrame_r.pack(side='right')
        #TimeLine
        tkinter.Label(StatusFrame_r, textvariable=self.var_Time, font=('等线', 10)).pack()
        #GoldLine
        tkinter.Label(StatusFrame_r, textvariable=self.var_Gold, font=('等线', 10)).pack()
        #LevelLine
        tkinter.Label(StatusFrame_r, textvariable=self.var_characterlevel, font=('等线', 10)).pack()
        #VigorLine
        tkinter.Label(StatusFrame_r, textvariable=self.var_charactervigor, font=('等线', 10)).pack()

        self.UpdateVar()
        return StatusFrame

    ##主界面
    def BuildHomeFrame(self):
        HomeFrame = tkinter.Frame(self.pack_leftframe)
        tkinter.Button(HomeFrame, text='炼金', width=10,
        command = lambda:self.StartAlchemy()).pack(side='left')

        tkinter.Button(HomeFrame, text='商店', width=10, 
        command = lambda:self.Rest()).pack(side='left')

        tkinter.Button(HomeFrame, text='休息', width=10, 
        command = lambda:self.Rest()).pack(side='left')

        tkinter.Button(HomeFrame, text='物品', width=10, 
        command = lambda:self.ShowItemFrame()).pack(side='left')
        return HomeFrame

    #物品栏相关
    def BuildItemFrame(self):
        ItemFrame = tkinter.Frame(self.HomeFrame, relief='ridge', borderwidth=2)
        if(self.Game.items):
            itemlabel = tkinter.Label(ItemFrame, text='物品栏')
            itemlabel.pack()
            for row in self.Game.items:
                tkinter.Label(ItemFrame, text = str(self.Game.conf.ItemDict[row['id']]['name'])+"x"+str(row['num'])).pack()
        else:
            itemlabel = tkinter.Label(ItemFrame, text='没有物品')
            itemlabel.pack()

        ExitButton = tkinter.Button(ItemFrame, text='返回', width=10, relief='ridge', 
        command=lambda:self.CloseItemFrame())
        ExitButton.pack(side='bottom')
        
        return ItemFrame

    def ShowItemFrame(self):
        if(self.ItemFrame == False):
            self.ItemFrame = self.BuildItemFrame()
            self.ItemFrame.pack()

    def CloseItemFrame(self):
        if(self.ItemFrame != False):
            for widget in self.ItemFrame.winfo_children():
                widget.destroy()
            self.ItemFrame.destroy()
            self.ItemFrame = False

    ##提示框相关
    def BuildAlertFrame(self):
        alertframe = tkinter.Frame(self.pack_rightframe)
        alertlabel = tkinter.Label(alertframe, textvariable=self.var_alerttext)
        alertlabel.config(fg="red")
        alertlabel.pack(side='top')
        return alertframe

    #更新frame中的变量
    #其他次级窗口更新时，可利用窗口传参statusframe实现同步更新
    def UpdateVar(self):
        self.var_Time.set(self.Game.time)
        self.var_Gold.set(self.Game.gold)
        self.var_characterlevel.set(self.Game.maincharacter.level)
        self.var_charactervigor.set(str(self.Game.maincharacter.vigor)+"/"+str(self.Game.maincharacter.vigor_max))
        self.var_alerttext.set(self.alerttext)

    #休息一回合
    def Rest(self):
        self.Game.game_Rest()
        self.alerttext = '摸了，爽诶'
        self.UpdateVar()

    def StartAlchemy(self):
        if(self.Game.game_StartAlchemy()):
            self.alerttext = '该堇业了'
        else:
            self.alerttext = '精力不足'
        self.UpdateVar()


