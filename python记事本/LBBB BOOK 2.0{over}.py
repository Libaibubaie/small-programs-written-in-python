import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

mywindow = tk.Tk()
mywindow.title("低配word1.1")
mywindow.geometry("400x300")
filename=""


def author():
    showinfo(title="作者", message="water66")


def power():
    showinfo(title="版权信息", message="water66")
    
def mypopup(event):
    editmenu.tk_popup(event.x_root,event.y_root)
    
def undo():
    global mytext
    mytext.event_generate("<<Undo>>")
    
def cut():
    global mytext
    mytext.event_generate("<<Cut>>")
    
def copy():
    global mytext
    mytext.event_generate("<<Copy>>")
    
def paste():
    global mytext
    mytext.event_generate("<<Paste>>")
    
def delete():
    global mytext
    mytext.event_generate("<<Backspace>>")
    
def myopen():
    global filename
    filename=filedialog.askopenfilename(defaultextension=".txt")
    if filename=="":
        filename=None
    else:
        mywindow.title("记事本"+os.path.basename(filename))
        mytext.delete(1.0,tk.END)
        f=open(filename,'r')
        mytext.insert(tk.INSERT,f.read())
        f.close()
        
def mysave():
    global filename
    f=filedialog.asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
    filename=f
    fh=open(f,'w')
    msg=mytext.get(1.0,tk.END)
    fh.write(msg)
    fh.close()
    mywindow.title("记事本"+os.path.basename(f))
    
def myhelp():
    print("按打开即可打开文件，单击另存为保存（PS：新建也行哦）")

def mysave2():
    global filename
    f=filedialog.asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
    filename=f
    fh=open(f,'w')
    msg=mytext.get(1.0,tk.END)
    fh.write(msg)
    fh.close()
    mywindow.title("记事本"+os.path.basename(f))
    
mytext = tk.Text(mywindow,undo=True)
mytext.pack(expand=1,fill=tk.BOTH)

savemenu = tk.Menu(mywindow)

savemenu.add_command(label="另存为",accelerator="Ctrl+Shift+S",command = mysave)
newtxt = tk.Menu(mywindow)

newtxt.add_command(label="文本文档",accelerator="Shift+W",command = mysave2)
filemenu = tk.Menu(mywindow)

filemenu.add_cascade(label="新建",menu=newtxt)

filemenu.add_checkbutton(label="打开",accelerator="Alt+D",command = myopen)
filemenu.add_cascade(label="保存", menu=savemenu,accelerator="B")
filemenu.add_separator()

filemenu.add_radiobutton(label="页面设置",state=tk.NORMAL)
filemenu.add_separator()

filemenu.add_radiobutton(label="退出",accelerator="Alt+F4")
editmenu = tk.Menu(mywindow)

editmenu.add_command(label="撤销",accelerator="Ctrl+Z",command=undo)
editmenu.add_separator()

editmenu.add_radiobutton(label="剪切",accelerator="Ctrl+X",command=cut)

editmenu.add_radiobutton(label="复制",accelerator="Ctrl+C",command=copy)

editmenu.add_command(label="粘贴",accelerator="Ctrl+V",command=paste)

editmenu.add_command(label="删除",accelerator="Ctrl+Backspace",command=delete)
editmenu.add_separator()

editmenu.add_checkbutton(label="全选",accelerator="Ctrl+Q")
mymenu = tk.Menu(mywindow)

mymenu.add_cascade(label="文件",menu=filemenu )

mymenu.add_cascade(label="编辑",menu=editmenu )

mymenu.add_cascade(label="格式")

mymenu.add_cascade(label="查看")

mymenu.add_cascade(label="帮助",accelerator="Ctrl+M",command = myhelp)
mytext.bind("<Button-3>",mypopup)

mywindow["menu"] = mymenu
