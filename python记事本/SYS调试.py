import  tkinter  as  tk   #导入Tkinter
import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
from  tkinter.scrolledtext  import ScrolledText  #导入ScrolledText
from tkinter.filedialog import *
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

#建立主窗口
root = ttk.Window("LBK SYS TEST", "darkly")
root.geometry('{}x{}+{}+{}'.format(800, 600, 100, 100))

#放几个按钮
frame=tk.Frame(root)
button1=tk.Button(frame,text='New File')
button1.config(fg="yellow",bg="black")
button2=tk.Button(frame,text='Open File')
button2.config(fg="yellow",bg="black")
button3=tk.Button(frame,text='Save as...')
button3.config(fg="yellow",bg="black")
button4=tk.Button(frame,text='Run File')
button4.config(fg="red",bg="black")
button5=tk.Button(frame,text='Clear')
button5.config(fg="yellow",bg="black")

button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
button5.pack(side=tk.RIGHT)
frame.pack(side=tk.TOP,fill=tk.BOTH)

#放置一个文本框
global textPad
textPad= ScrolledText(bg='black',fg='LimeGreen')
textPad.pack(fill=tk.BOTH, expand=1)
textPad.focus_set()

global filename
filename='newfile.py'

#实现按钮功能
def btnfunc01():  #新文件
    global textPad,filename
    textPad.delete(1.0,tk.END)
    filename='newfile.py'

def btnfunc02(): #读取文件
    global textPad,filename
    filename2 = askopenfilename(defaultextension='.py')
    if filename2 != '':
        textPad.delete(1.0,tk.END)#delete all
        f = open(filename2,'r',encoding='utf-8',errors='ignore')
        textPad.insert(1.0,f.read())
        f.close()
        filename=filename2


def btnfunc03(): #另存文件
    global textPad,filename
    filename = asksaveasfilename(initialfile = filename,defaultextension ='.py')
    if filename != '':
        fh = open(filename,'w',encoding='utf-8',errors='ignore')
        msg = textPad.get(1.0,tk.END)
        fh.write(msg)
        fh.close()

#为按钮设置功能
button1['command']=lambda:btnfunc01()
button2['command']=lambda:btnfunc02()
button3['command']=lambda:btnfunc03()

##为信息框设置一个容器
frame2=tk.LabelFrame(root,text='Text',bg='black',fg='Red',height=100)
frame2.pack(fill=tk.BOTH, expand=1)

global textMess

#放置一个文本框作为信息输出窗口
textMess= ScrolledText(frame2,bg='black',fg='Blue', height=10)
textMess.pack(fill=tk.BOTH, expand=1)
##清空信息窗
def clearMess():
    global textMess
    textMess.delete(1.0,tk.END)

#用户输出信息
def myprint(txt):
    global textMess
    if textMess != None :
        textMess.insert(tk.END, txt)
        textMess.see(tk.END)

#输出彩色信息
def colorprint(txt,color='black'):
    global textMess
    if textMess != None :
        if color!='black':
            textMess.tag_config(color, foreground=color)   
        textMess.insert(tk.END, txt,color)
        textMess.see(tk.END)

#运行用户程序
def runpy():
    global textPad,textMess
    try:
        msg = textPad.get(1.0,tk.END)
        mg=globals()
        ml=locals()
        exec(msg,mg,ml)
    except Exception as e:
        colorprint('\n<LBK CONSOLE||Runtime Error>'+str(e)+'\n','Blue')
        
button4['command']=lambda:runpy()
button5['command']=lambda:clearMess()

root.mainloop() #进入Tkinter消息循环
