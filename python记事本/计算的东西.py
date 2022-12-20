import tkinter as tk
import tkinter.messagebox
import pickle
import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText
import datetime
import pathlib
from queue import Queue
from threading import Thread
from tkinter.filedialog import askdirectory
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import utility
#===================================================================================
#完美算数教室
#===================================================================================


root = ttk.Window("LBK MATH", "lbkoline2.4")
root.minsize(320,440) #大小尺寸
shownum = tkinter.StringVar()
shownum.set(0)
# ===================================================================================
numstrlist=[]#存储数字 符号
isjisuan=False#运算标志
#==================================================================
#数据触发事件
#==================================================================
def pressnum(num):#按下数字
    global isjisuan
    if isjisuan==True:
        shownum.set('0')
        isjisuan=False
    oldnum=shownum.get()
    if oldnum=='0':#旧数字是否为0
        shownum.set(num)
    else:
        if num =='+/-':
            if oldnum.startswith('-'):
                shownum.set(oldnum[1:])
            else:
                shownum.set('-'+oldnum)
        else:
            shownum.set(oldnum+num)
#==================================================================
#该函数主要实现数据加减符号的操作
#==================================================================
def presssign(sign):#按下加减符号
    global numsrtlist
    global isjisuan
    oldnum=shownum.get()
    numstrlist.append(oldnum)
    numstrlist.append(sign)
    isjisuan=True
    print(numstrlist)
#==================================================================
#该函数主要实现计算器的等的操作符
#==================================================================
def equal(sign):
    global numstrlist
    if sign=='=':
        oldnum =shownum.get()
        numstrlist.append(oldnum)
        print(numstrlist)
        resu1 =''.join(numstrlist)
        result =eval(resu1)
        print(result)
        shownum.set(result)
        numstrlist.clear()
    if sign =='1/x':
        oldnum = shownum.get()
        result =1/float(oldnum)
        print(result)
        shownum.set(result)
    if sign =='√':
        oldnum = shownum.get()
        result = math.sqrt(float(oldnum))
        print(result)
        shownum.set(result)
#==================================================================
#该函数主要实现的是数据的清空操作
#==================================================================
def gui0():  #清空数据
    global numstrlist
    global isjisuan
    numstrlist.clear()
    isjisuan=False
    shownum.set(0)
# ===================================================================================
#文本框输入
# ===================================================================================
label=tkinter.Label(root,textvariable=shownum,bg='black',fg='red',font=('宋体',20),anchor='e',bd=5)
label.place(x=15,y=10,width=280,height=50)
# ===================================================================================
#第一行
# ===================================================================================
btn1 =tkinter.Button(text ='MC',bg='black',fg='Yellow',bd=2)#Memory Clear 清除存储器中的数值
btn1.place(x=10,y =70,width =50,height=50)
btn2 =tkinter.Button(text ='MR',bg='black',fg='Yellow',bd=2)#Memory Read 存储器读出
btn2.place(x=70,y =70,width =50,height=50)
btn3 =tkinter.Button(text ='MS',bg='black',fg='Yellow',bd=2)#Memory Save 存入存储器
btn3.place(x=130,y =70,width =50,height=50)
btn4 =tkinter.Button(text ='M+',bg='black',fg='Yellow',bd=2)#Memory Plus 将数值与存储器中的数值相加
btn4.place(x=190,y =70,width =50,height=50)
btn5 =tkinter.Button(text ='M-',bg='black',fg='Yellow',bd=2)
btn5.place(x=250,y =70,width =50,height=50)
# ===================================================================================
#第二行
# ===================================================================================
btn2_1 =tkinter.Button(text ='del',bg='black',fg='Yellow',bd=3)
btn2_1.place(x=10,y =130,width =50,height=50)
btn2_2 =tkinter.Button(text ='CE',bg='black',fg='Yellow',bd=3,command=lambda:gui0())#CE是清除全部数字，但不影响以前的计算
btn2_2.place(x=70,y =130,width =50,height=50)
btn2_3 =tkinter.Button(text ='C',bg='black',fg='Yellow',bd=3,command=lambda:gui0())#C健是重新开始计算，和ESC键是一样的功能
btn2_3.place(x=130,y =130,width =50,height=50)
btn2_4 =tkinter.Button(text ='+/-',bg='black',fg='blue',bd=3,command=lambda:pressnum('+/-'))
btn2_4.place(x=190,y =130,width =50,height=50)
btn2_5 =tkinter.Button(text ='√',bg='black',fg='blue',bd=3,command=lambda:equal('√'))#--------√开平方
btn2_5.place(x=250,y =130,width =50,height=50)
# ===================================================================================
#第三行
# ===================================================================================
btn3_1 =tkinter.Button(text ='7',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('7'))
btn3_1.place(x=10,y =190,width =50,height=50,)
btn3_2 =tkinter.Button(text ='8',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('8'))
btn3_2.place(x=70,y =190,width =50,height=50)
btn3_3 =tkinter.Button(text ='9',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('9'))
btn3_3.place(x=130,y =190,width =50,height=50)
btn3_4 =tkinter.Button(text ='÷',bg='black',fg='blue',command=lambda:presssign('/'))
btn3_4.place(x=190,y =190,width =50,height=50)
btn3_5 =tkinter.Button(text ='%',bg='black',fg='blue',command=lambda:presssign('%'))
btn3_5.place(x=250,y =190,width =50,height=50)
# ===================================================================================
#第四行
# ===================================================================================
btn4_1 =tkinter.Button(text ='4',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('4'))
btn4_1.place(x=10,y =250,width =50,height=50)
btn4_2 =tkinter.Button(text ='5',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('5'))
btn4_2.place(x=70,y =250,width =50,height=50)
btn4_3 =tkinter.Button(text ='6',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('6'))
btn4_3.place(x=130,y =250,width =50,height=50)
btn4_4 =tkinter.Button(text ='*',bg='black',fg='blue',command=lambda:presssign('*'))
btn4_4.place(x=190,y =250,width =50,height=50)
btn4_5 =tkinter.Button(text ='1/x',bg='black',fg='blue',command=lambda:equal('1/x'))#倒数
btn4_5.place(x=250,y =250,width =50,height=50)
# ===================================================================================
#第五行
# ===================================================================================
btn5_1 =tkinter.Button(text ='1',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('1'))
btn5_1.place(x=10,y =310,width =50,height=50)
btn5_2 =tkinter.Button(text ='2',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('2'))
btn5_2.place(x=70,y =310,width =50,height=50)
btn5_3 =tkinter.Button(text ='3',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('3'))
btn5_3.place(x=130,y =310,width =50,height=50)
btn5_4 =tkinter.Button(text ='-',bg='black',fg='blue',command=lambda:presssign('-'))
btn5_4.place(x=190,y =310,width =50,height=50)
btn5_5 =tkinter.Button(text ='=',bg='black',fg='blue',command=lambda:equal('='))
btn5_5.place(x=250,y =310,width =50,height=110)
 # ===================================================================================
#第六行
# ===================================================================================
btn6_1 =tkinter.Button(text ='0',bg='black',fg='LimeGreen',bd=3,command=lambda:pressnum('0'))
btn6_1.place(x=10,y =370,width =110,height=50)
btn6_3 =tkinter.Button(text ='.',bg='black',fg='blue',command=lambda:pressnum('.'))
btn6_3.place(x=130,y =370,width =50,height=50)
btn6_4 =tkinter.Button(text ='+',bg='black',fg='blue',command=lambda:presssign('+'))
btn6_4.place(x=190,y =370,width =50,height=50)
# ===================================================================================
root.mainloop()
# ==============================================================================
