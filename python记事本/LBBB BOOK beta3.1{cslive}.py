# -*- coding: utf-8 -*-
import  tkinter  as  tk   #导入Tkinter
import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
import pickle

from tkinter.messagebox import *
from tkinter.filedialog import *

from HP_formula import * #导入小白公式模块


mytitle='小白量化中文Python研学实控系统 Vre 3.00'
#建立主窗口
root=htk.MainWindow(title=mytitle,x=100,y=200,w=1200, h=700)
root.iconbitmap('ico/cp64.ico')  #设置应用程序图标
root.SetCenter()  #移动到屏幕中央
##获取窗口信息
screenwidth = root.winfo_screenwidth()  #获取屏幕宽度（单位：像素）
screenheight = root.winfo_screenheight()  #获取屏幕高度（单位：像素）
winw= root.winfo_width()   #获取窗口宽度（单位：像素）
winh = root.winfo_height()  #获取窗口高度（单位：像素）

#建立窗口菜单
menus = [['文件',['执行程序','-','新建','打开','运行','-','保存','另存为']],\
         ['编辑',['撤销','重做','-','剪切','复制','粘贴','清除','-','全选']],\
         ['显示',['绘图','表格']],\
         ['程序',['运行','转中文','转英文']],\
         ['项目',['项目目录','系统设置','恢复环境变量']],\
         ['数据',['连接行情服务器','断开行情服务器','下载股票代码表','下载财务数据',\
                '下载板块数据']],\
         ['帮助',['关于软件','项目缩略图','退出']]]
mainmenu=htk.windowMenu(root,menus) #窗口菜单

tabControl = htk.ClosableNotebook(root) #创建Notebook
tab1 = tk.Frame(tabControl,bg='#1E488F')  #增加新选项卡tab1
tabControl.add(tab1, text='研学中心')  #把新选项卡增加到Notebook
tabControl.pack(expand=1, fill="both")  #使用pack方法显示
tabControl.select(tab1) #选择tab1

#分割窗口为左右两部分
#建立可分割区域paned
paned= tk.PanedWindow(tab1,orient=tk.HORIZONTAL,showhandle=True, \
                    sashrelief=tk.SUNKEN,sashwidth=1)  #默认是左右分布的
paned.pack(fill=tk.BOTH, expand=1) #放到主窗口，上下左右缩放

#选择目录
def selectdirectory():
    path_ = askdirectory()
    tree.clear()
    tree.load_path(path_ ) #为树控件加载指定的目录树


#树鼠标双击事件
def treeDoubleClick(event):
    #print(event)
    item = tree.tree.selection()[0]
    i2=tree.tree.parent(item)
    s2=""
    while i2!="":
        s2=tree.tree.item(i2, "text")+'\\'+s2
        i2=tree.tree.parent(i2)
    txt2=s2+tree.tree.item(item, "text")
    if txt2[-4:]=='.txt' or txt2[-3:]=='.py':
        ucode.loadfile(txt2)
        tabControl2.tab(0, text=ucode.filename)

def setlabel():
    tabControl2.tab(0, text=ucode.filename)

#左画面设计
ttabControl = ttk.Notebook(paned)          # Create Tab Control
ttab1 = ttk.Frame(ttabControl)            # Add a third tab
ttabControl.add(ttab1, text='工程目录')      # Make second tab visible
paned.add(ttabControl)
paned.paneconfig(ttabControl,width=200)

tree = htk.Tree(ttab1,width=200)
tree.load_path('./') #为树控件加载指定的目录树
tree.pack(expand = 1, fill = tk.BOTH)
tree.usepop=treeDoubleClick  #绑定双击事件

#在左右可调区域中创建，可上下调整区域paned2
paned2 = tk.PanedWindow(paned,orient=tk.VERTICAL, showhandle=True, sashrelief=tk.SUNKEN,width=int((winw-300)/2),sashwidth=1)
paned.add(paned2)

#tabControl = htk.ClosableNotebook(paned2)  #创建Notebook
tabControl2 = ttk.Notebook(paned2) 
tab = tk.Frame(tabControl2,bd=0,background='black')
tabControl2.add(tab, text='newfile.py')
#在选项卡中建立代码编辑器
ucode=ide.Codeedit(tab,fontsize=12,bg='black')   #代码编辑框
tabControl2.pack(fill=tk.BOTH, expand=1)
ucode.setlabel=setlabel
ucode.outcolor='white'
ucode.outcolor2='white'
ucode.ispop=True  #动态提示
paned2.add(tabControl2)
paned2.paneconfig(tabControl2,heigh=400)
root.ucb=ucode.Callback

#建立分割区域paned3
paned3 = tk.PanedWindow(paned2,orient=tk.VERTICAL, showhandle=True, sashrelief=tk.SUNKEN,width=int((winw-300)/2),bg='black',sashwidth=1)
paned2.add(paned3)

##为信息框设置一个容器
frame2=tk.LabelFrame(paned3,text='信息框',height=100)
frame2.pack(fill=tk.BOTH, expand=1)

umess=ide.PythonCMD(frame2,ipy="ipython",py="ipython ",fontsize=12,bg='#5a5a5a')
umess.pack(expand=1,fill=tk.BOTH)
paned3.paneconfig(frame2,heigh=200)

htk.ttmsg=umess.text  #绑定信息输出变量，
ucode.outmess=htk.ttmsg   #设置代码输出信息框
#htk.ttmsg['bg']='#7a7a7a'  #输出窗底色
htk.ttmsg['fg']='white'    #输出框字体颜色
htk.ttmsg['insertbackground']='magenta'    #输出框光标颜色

#创建状态栏
status=htk.StatusBar(root)    #建立状态栏
status.pack(side=tk.BOTTOM, fill=tk.X)  #把状态栏放到最底部
status.demo()

keyvars=[g.root,g.mainmenu,g.tabControl,g.tab1,g.tab2,g.tab3,g.tab4,g.tab5,g.tab6,g.tab7,g.tab8,g.tab9]
def resetvar():
    [g.root,g.mainmenu,g.tabControl,g.tab1,g.tab2,g.tab3,g.tab4,g.tab5,g.tab6,g.tab7,g.tab8,g.tab9]=keyvars

##设置菜单功能的功能
mainmenu.set('文件','执行程序',command=ucode.runpy)
mainmenu.set('文件','新建',command=ucode.newfile)
mainmenu.set('文件','打开',command=ucode.openfile)
mainmenu.set('文件','运行',command=ucode.runuc)
mainmenu.set('文件','保存',command=ucode.savefile)
mainmenu.set('文件','另存为',command=ucode.saveas)
mainmenu.set('编辑','撤销',command=ucode.undo)
mainmenu.set('编辑','重做',command=ucode.redo)
mainmenu.set('编辑','剪切',command=ucode.cut)
mainmenu.set('编辑','复制',command=ucode.copy)
mainmenu.set('编辑','粘贴',command=ucode.paste)
mainmenu.set('编辑','全选',command=ucode.selectall2)
mainmenu.set('程序','运行',command=ucode.runuc)
mainmenu.set('程序','转中文',command=ucode.pyetoc)
mainmenu.set('程序','转英文',command=ucode.pyctoe)
mainmenu.set('帮助','项目缩略图',command=root.save)
mainmenu.set('项目','项目目录',command=selectdirectory)
mainmenu.set('项目','恢复环境变量',command=resetvar)
#全局初始化
g.title=mytitle
g.root=root
g.mainmenu=mainmenu
g.ucode=ucode
g.tabControl=tabControl
g.tab1=tab  #工作台
keyvars=[g.root,g.mainmenu,g.tabControl,g.tab1,g.tab2,g.tab3,g.tab4,g.tab5,g.tab6,g.tab7,g.tab8,g.tab9]
def setvar():
    global keyvars
    keyvars=[g.root,g.mainmenu,g.tabControl,g.tab1,g.tab2,g.tab3,g.tab4,g.tab5,g.tab6,g.tab7,g.tab8,g.tab9]
def resetvar():
    global keyvars
    [g.root,g.mainmenu,g.tabControl,g.tab1,g.tab2,g.tab3,g.tab4,g.tab5,g.tab6,g.tab7,g.tab8,g.tab9]=keyvars

setvar()
tabControl.ufun=resetvar
root.mainloop()      #进入Tkinter消息循环
