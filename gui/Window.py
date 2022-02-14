import tkinter
#游戏主界面，没有内部划分
#定义框架切换[1=>mainframe, 2=>gameframe, 3=>settingframe, 4=>infoframe, 5=>loadframe]
from gui.GameView import *

class Window:

    @staticmethod
    def BuildMainWindow():
        MainWindow = tkinter.Tk()
        MainWindow.title("not-just-alchemist")
        MainWindow.geometry("800x500")
        return MainWindow

    def BuildMainFrame(self):
        #主页面的框架
        MainFrame = tkinter.Frame(self.MainWindow)
        #按钮
        StartLine = tkinter.Label(MainFrame, text="not - just - alchemist", font=('等线', 32), height=5)
        StartButton = tkinter.Button(MainFrame, text="从头开始", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(4))
        ReadButton = tkinter.Button(MainFrame, text="读取存档", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(3))
        SettingButton = tkinter.Button(MainFrame, text="游戏设置", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(1))
        InfoButton = tkinter.Button(MainFrame, text="关于", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(2))
        ExitButton = tkinter.Button(MainFrame, text="退出", font=('等线', 16), width=15, relief='flat', 
        command = self.MainWindow.quit)
    
    #height是按行高算的，width是按英文空格算的
    #布局
        StartLine.pack()
        StartButton.pack()
        ReadButton.pack()
        SettingButton.pack()
        InfoButton.pack()
        ExitButton.pack()
        return MainFrame

    def BuildGameFrame(self):
        GameFrame = tkinter.Frame(self.MainWindow)
        gameview = GameView(GameFrame)
        
        tkinter.Button(gameview.pack_rightframe, text="返回", font=('等线', 12), width=10, relief='ridge', 
        command=lambda:self.SwitchFrame(0)).pack(side='bottom')
        tkinter.Button(gameview.pack_rightframe, text="保存", font=('等线', 12), width=10, relief='ridge', 
        command=lambda:self.SwitchFrame(0)).pack(side='bottom')
        tkinter.Button(gameview.pack_rightframe, text="读取", font=('等线', 12), width=10, relief='ridge', 
        command=lambda:self.SwitchFrame(0)).pack(side='bottom')
        return GameFrame

    def BuildSettingFrame(self):
        SettingFrame = tkinter.Frame(self.MainWindow)

        StartLine = tkinter.Label(SettingFrame, text="没什么可设置的", font=('等线', 32), height=5)
        ReturnButton= tkinter.Button(SettingFrame, text="返回", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(0))

        StartLine.pack()
        ReturnButton.pack()
        return SettingFrame

    def BuildInfoFrame(self):
        InfoFrame = tkinter.Frame(self.MainWindow)
        InfoText = tkinter.Text(InfoFrame, height=5)
        InfoText.insert('insert',"项目地址 \n")
        ReturnButton= tkinter.Button(InfoFrame, text="返回", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(0))

        InfoText.pack()
        ReturnButton.pack()
        return InfoFrame

    def BuildLoadFrame(self):
        LoadFrame = tkinter.Frame(self.MainWindow)
        StartLine = tkinter.Label(LoadFrame, text="暂不支持存档功能，但是可以看看", font=('等线', 16), height=5)
        ReturnButton= tkinter.Button(LoadFrame, text="返回", font=('等线', 16), width=15, relief='flat', 
        command=lambda:self.SwitchFrame(0))
        StartLine.pack()
        ReturnButton.pack()
        return LoadFrame

    def SwitchFrame(self, nextframe):
        self.Frames[self.CurrentFrame].pack_forget()
        self.CurrentFrame = nextframe
        self.Frames[self.CurrentFrame].pack(expand='yes', fill='both')

    def __init__(self):
        self.MainWindow = self.BuildMainWindow()
        self.MainFrame = self.BuildMainFrame()
        self.GameFrame = self.BuildGameFrame() #gameframe只能在输入存档号之后生成,暂时不实现
        self.SettingFrame = self.BuildSettingFrame()
        self.InfoFrame = self.BuildInfoFrame()
        self.LoadFrame = self.BuildLoadFrame()
        self.Frames = [self.MainFrame, self.SettingFrame, self.InfoFrame, self.LoadFrame, self.GameFrame]

        self.CurrentFrame = 0
        self.MainFrame.pack()
        self.MainWindow.mainloop()
