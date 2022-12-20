# Tkinter GUI可视化生成代码验证程序.
import tkinter as tk
import tkinter as ttk
import tkinter.tix as tix 
from tkinter.constants import *


s1='''
import tkinter as tk
import tkinter as ttk
import tkinter.tix as tix 
from tkinter.constants import *

root = tix.Tk()   #主窗口root
root.title("可视化设计结果")
'''

s2='''
root.mainloop()
'''

if __name__ == '__main__':
    root = tix.Tk()   #主窗口root
    root.title("可视化设计")
   
    f0=tk.Toplevel(root)  #可视化子窗
    f0.title('弹出窗口')  #Tkinter中设置窗口标题方法
    
    top=htk.resizewidget(f0,800,600)  #建立可调部件区域

    f=tk.Button(top)   #创建一个部件
    f.place(x=30, y=150, width=190, height=100)
    top.setwidget(f)  #加入可调部件
    
    l=tk.Label(top,text='Label')
    l.place(x=130, y=150, width=120, height=30)
    top.setwidget(l)  #加入可调部件

    def btn_cmd():
        print('窗口坐标(%d,%d)'%(f0.winfo_x(),f0.winfo_y()))
        print('窗口宽高(%d,%d)'%(f0.winfo_width() ,f0.winfo_height()))
        print('\n部件1坐标')
        x,y,width,height=top.readplace(top.win[0])
        print('组件坐标:',x,y)
        print('组件宽高:',width ,height)
        print('\n部件2坐标')
        x,y,width,height=top.readplace(top.win[1])
        print('组件坐标:',x,y)
        print('组件宽高:',width ,height)
        s=s1+'\n'
        ss="root.geometry(\'{}x{}+{}+{}\'.format(%d,%d, %d, %d))  #改变窗口位置和大小"%(f0.winfo_width(),\
            f0.winfo_height(),f0.winfo_x(),f0.winfo_y())
        s=s+ss+'\n'
        for i in range(top.m):
            x,y,width,height=top.readplace(top.win[i])
            w=top.readwidget(top.win[i])
            if w=='Label':
                ss='f%d=tk.%s(root,text=\'label%d\')'%(i,w,i)
            else:
                ss='f%d=tk.%s(root)'%(i,w)
            s=s+ss+'\n'
            ss='f%d.place(x='%i
            ss=ss+x+',y='+y+',width='+width+' ,height='+height+')'
            s=s+ss+'\n'
        s=s+s2
        print('\n生成代码:\n')
        print(s)

    btn=tk.Button(root,text='生成代码',command=btn_cmd)
    btn.place(x=10,y=10)
    root.mainloop()
