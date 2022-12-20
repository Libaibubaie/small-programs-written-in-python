import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import scrolledtext
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog
import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
from  tkinter.scrolledtext  import ScrolledText  #导入ScrolledText
from tkinter.filedialog import *
import  tkinter  as  tk   #导入Tkinter
import  tkinter.ttk  as  ttk   #导入Tkinter.ttk
from  tkinter.scrolledtext  import ScrolledText  #导入ScrolledText
from tkinter.filedialog import *
import webbrowser
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
import time
import os

#style = Style()
#style = Style(theme='sandstone')
#想要切换主题，修改theme值即可，有以下这么多的主题，自己尝试吧：['vista', 'classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam', 'alt', 'solar', 'minty', 'litera', 'united', 'xpnative', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']
#TOP6 = style.master
#这两行代码在自己原基础的代码上加入即可，放在代码的最开端部分，也就是在窗口创建代码之前

def draw():
    os.system("draw.py")
    
def worker():
    webbrowser.open("https://space.bilibili.com/1792020975")

def quit():
    top.destroy()
    
def close():
    top.quit()

def SYS():
    top.destroy()
    os.system("SYS调试.py")
def math():
    os.system("计算的东西.py")
def save2():
    showinfo(title="方案二", message="只支持快捷键，请先全屏，接着按下prtscr(win10有效，不过会录下任务栏，正在完善),最后，你就可以在剪切板看到它了！")

def get_time():

    '''显示当前时间'''

    global time1
    time1 = ''
    time2 = time.strftime('%Y-%m-%d %H:%M:%S')
    # 能动态显示系统时间
    if time2 != time1:
        time1 = time2
        clock = Label(top, text=time1, font=9)
        clock.configure(text=time2)
        clock.config(bg='black',fg='GreenYellow')
        clock.place(x=580, y=1)
        clock.after(200,get_time)


  

def choosepic():
  path_=askopenfilename()
  path.set(path_)
  img_gif=Tkinter.PhotoImage(file='2233.gif')
  l1.config(image=img_gif)
def which():
    which = tkinter.colorchooser.askcolor()[1]
    which = tk.Label(top,textvariable=which,width=1,relief=tk.SUNKEN,anchor=tk.N,font=18)
    which.pack(side=tk.LEFT,fill=tk.Y)
def update_line_num():
    if self.is_show_line_num.get():
        #获取所有行
        #top, col = self.context_text.index(END).split('. ')
        #列举每行的行号
        Line_num_content = "\n".join([str(i) for i in range(1, int(row))])
        self.Line_number_bar.config(state="normal")
        self.Line_number_bar.delete(1.0, END)
        self.line_number_bar.insert(1.0, Line_num_content)
        self.Line_number_bar.config(state='disable')
    else:
        self.Line_number_bar.config(state=' normal' )
        self.Line_number_bar.delete(1.0,END)
        self.Line_number_bar.config(state='disable')


def help():
    #print("(这只是一个简单的帮助)由于tk部分指令在3.8下无法正常调用，所以撤销和重做暂时实现不了，尝试修复后无果，为了保证代码的完整性，我们将会保留他们，但请你知道，它们没有任何用处(这是计划的一部分)")
    showinfo(title="作者", message="我用tkinter写出了bug，但bug刚好满足了tkinter、、、\n使用时间功能时记得自己换行(考虑到用户手感，正经人谁写那儿么长)\n(这只是一个简单的帮助)由于tk部分指令在3.8下无法正常调用，所以撤销和重做暂时实现不了，尝试修复后无果，为了保证代码的完整性，我们将会保留他们，但请你知道，它们没有任何用处(这是计划的一部分)\n行数其实只是一个标尺，毕竟写程序要缩进很麻烦，比且目前无法让其一起滚动，只是一个标尺！！！\n哦，对了，我们在测试版总是会附带一个编译器，不过它似乎不太稳定，正式版是不会考虑增加任何一个测试项的,不过即使是sc版也不建议你使用它，它会把你的电脑黑屏，总之，在sc版本，小心点总是是好的=)\n啊，总之你必须会在必要的时候结束进程=)\n祝你好运=）")


def author():
    showinfo(title="作者", message="Libaibubai_official(Libaibubai@163.com)")


def power():
    showinfo(title="版权信息", message="Libaibubai_official")

def another():
    showinfo(title="作者的话", message="给程序以bug，而不是给bug以程序```")



def new_file(*args):
    global top, filename, textPad
    top.title("未命名文件")
    filename = None
    textPad.delete(1.0,tk.END)


def open_file(*args):
    global filename
    filename = askopenfilename(defaultextension=".txt")
    if filename == "":
        filename = None
    else:
        top.title(""+os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r', encoding="utf-8")
        textPad.insert(1.0, f.read())
        f.close()


def click_open(event):
    global filename
    top.title("" + os.path.basename(filename))
    textPad.delete(1.0, END)
    f = open(filename, 'r', encoding="utf-8")
    textPad.insert(1.0, f.read())
    f.close()


def save(*args):
    global filename
    try:
        f=open(filename, 'w', encoding="utf-8")
        msg=textPad.get(1.0, 'end')
        f.write(msg)
        f.close()
    except:
        save_as()


def save_as(*args):
    global filename
    f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
    filename = f
    fh = open(f, 'w', encoding="utf-8")
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    top.title(""+os.path.basename(f))


def rename(newname):
    global filename
    name = os.path.basename(os.path.splitext(filename)[0])
    oldpath = filename
    newpath = os.path.dirname(oldpath)+'/'+newname+'.txt'
    os.rename(oldpath, newpath)
    filename = newpath
    refresh()
        
        
def rename_file(*args):
    global filename
    t = Toplevel()
    t.geometry("260x80+200+250")
    t.title('重命名')
    frame = Frame(t)
    frame.pack(fill=X)
    lable = Label(frame, text="文件名")
    lable.pack(side=LEFT, padx=5)
    var = StringVar()
    e1 = Entry(frame, textvariable=var)
    e1.pack(expand=YES, fill=X, side=RIGHT)
    botton = Button(t, text="确定", command=lambda: rename(var.get()))
    botton.pack(side=BOTTOM, pady=10)


def delete(*args):
    global filename, top
    choice = askokcancel('提示', '要执行此操作吗')
    if choice:
        if os.path.exists(filename):
            os.remove(filename)
            textPad.delete(1.0, END)
            top.title("LBK文档控制台")
            filename = ''


def cut():
    global textPad
    textPad.event_generate("<<Cut>>")


def copy():
    global textPad
    textPad.event_generate("<<Copy>>")


def paste():
    global textPad
    textPad.event_generate("<<Paste>>")


def undo():
    global textPad
    textPad.event_generate("<<Undo>>")


def redo():
    global textPad
    textPad.event_generate("<<Redo>>")


def select_all():
    global textPad
    textPad.tag_add("sel", "1.0", "end")


def find(*agrs):
    global textPad
    t = Toplevel(top)
    t.title("查找")
    t.geometry("260x60+200+250")
    t.transient(top)
    Label(t, text="查找：").grid(row=0, column=0, sticky="e")
    v = StringVar()
    e = Entry(t, width=20, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    e.focus_set()
    c = IntVar()
    Checkbutton(t, text="不区分大小写", variable=c).grid(row=1, column=1, sticky='e')
    Button(t, text="查找所有", command=lambda: search(v.get(), c.get(), textPad, t, e)).grid\
        (row=0, column=2, sticky="e"+"w", padx=2, pady=2)
    
    def close_search():
        textPad.tag_remove("match", "1.0", END)
        t.destroy()
    t.protocol("WM_DELETE_WINDOW", close_search)


def mypopup(event):
    global editmenu
    editmenu.tk_popup(event.x_root, event.y_root)


def search(needle, cssnstv, textPad, t, e):
    textPad.tag_remove("match", "1.0", END)
    count = 0
    if needle:
        start = 1.0 # 1.0代表第一行第一个字符，小数点前表示行数，小数点后表示光标所在字符数位数
        while True:
            pos = textPad.search(needle, start, nocase=cssnstv, stopindex=END)
            if not pos:
                break
            strlist = pos.split('.')
            left = strlist[0]
            right = str(int(strlist[1])+len(needle))
            lastpos = left+'.'+right
            textPad.tag_add("match", pos, lastpos)
            count += 1
            start = lastpos
            textPad.tag_config('match', background="yellow")
        e.focus_set()
        t.title(str(count)+"个被匹配")


def refresh():
    global top, filename
    if filename:
        top.title(os.path.basename(filename))
    else:
        top.title("LBK")





top = ttk.Window("LBK Text Reader", "classic")


menu = tk.Menu(top,tearoff=False)

# 文件功能
filemenu = tk.Menu(menu)
filemenu.add_command(label="新建", accelerator="Ctrl+N", command=new_file)
filemenu.add_command(label="打开", accelerator="Ctrl+O", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="保存(方案一)", accelerator="Ctrl+S", command=save)
filemenu.add_command(label="保存(方案二)", accelerator="None", command=save2)
filemenu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=save_as)
filemenu.add_command(label="重命名", accelerator="Ctrl+R", command=rename_file)
filemenu.add_separator()
filemenu.add_command(label="删除", accelerator="Ctrl+D", command=delete)
filemenu.add_command(label="关闭", accelerator="None", command=close)
filemenu.add_command(label="退出", accelerator="None", command=quit)
menu.add_cascade(label="文件(第一目录)", menu=filemenu)

#SYS TEST
filemenu = tk.Menu(menu)
filemenu.add_command(label="时间", accelerator="None", command=get_time)
filemenu.add_command(label="计算器", accelerator="None", command=math)
filemenu.add_command(label="自带调试工具(不稳定)", accelerator="None", command=SYS)
filemenu.add_command(label="画板", accelerator="None", command=draw)
menu.add_cascade(label="小组件", menu=filemenu)

# 编辑功能
editmenu = tk.Menu(top)
editmenu.add_command(label="撤销", accelerator="Ctrl+Z", command=undo)
editmenu.add_command(label="重做", accelerator="Ctrl+Y", command=redo)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl+V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl+F", command=find)
editmenu.add_command(label="全选", accelerator="Ctrl+A", command=select_all)
menu.add_cascade(label="编辑", menu=editmenu)

#工具栏
var_status = tk.StringVar()
var_format = "LBK 4.0 100% [#utf-8]|Number Of Character：{}"
var_status.set(var_format.format(0))
# 状态栏
status = tk.Label(top, textvariable=var_status,bg='black',fg='Yellow',bd=2, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

var_line = tk.StringVar()
# 行数
line_label = tk.Label(top, width=2, bg='black',fg='red', textvariable=var_line, anchor=tk.N, font=10)
line_label.pack(side=tk.LEFT, fill=tk.Y)
###核心代码(没错，就这两行)###
# 文本编辑区域
textPad = tk.Text(top, undo=True, bg='black',fg='LimeGreen',font=18)
textPad.pack(expand=tk.YES, fill=tk.BOTH)
###不要修改哦=)(自定义颜色除外)###


"""记事本事件 2"""


def status_func(key):
    """设置状态栏信息"""
    contents = textPad.get(1.0, tk.END)
    length = contents.count('\n')
    char = contents.replace('\n', "")
    char_len = len(char)
    var_status.set(var_format.format(char_len))

    """设置显示行数的内容"""
    line_str = ''
    for i in range(1, length + 1):
        line_str += f"{i}\n"
    var_line.set(line_str)




# 绑定状态栏
textPad.bind('<Key>', status_func)

# 滑动栏
scroll = tk.Scrollbar(textPad, cursor="circle")
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)



# 关于功能
aboutmenu = tk.Menu(top)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="作者的话", command=another)
aboutmenu.add_command(label="作者主页", command=worker)
aboutmenu.add_separator()
aboutmenu.add_command(label="版权", command=power)
aboutmenu.add_command(label="帮助", command=help)
menu.add_cascade(label="关于", menu=aboutmenu)

top['menu'] = menu



# 热键绑定
textPad.bind("<Control-N>", new_file)
textPad.bind("<Control-n>", new_file)
textPad.bind("<Control-O>", open_file)
textPad.bind("<Control-o>", open_file)
textPad.bind("<Control-S>", save)
textPad.bind("<Control-s>", save)
textPad.bind("<Control-D>", delete)
textPad.bind("<Control-d>", delete)
textPad.bind("<Control-R>", rename_file)
textPad.bind("<Control-r>", rename_file)
textPad.bind("<Control-A>", select_all)
textPad.bind("<Control-a>", select_all)
textPad.bind("<Control-F>", find)
textPad.bind("<Control-f>", find)

textPad.bind("<Button-3>", mypopup)

#我用tkinter写出了bug，但是刚好满足了需求
#tkinter.colorchooser.askcolor()[1]
def center_window(top,w, h):
    # 获取屏幕 宽、高
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    app.geometry('%dx%d' % (w, h))
    
#控制是否允许画图的变量，1：允许，0：不允许
yesno = tk.IntVar(value=0)
#控制画图类型的变量，1：曲线，2：直线，3：矩形，4：文本，5：橡皮 6：圆形
what = tk.IntVar(value=1)
#记录鼠标位置的变量
X = tk.IntVar(value=0)
Y = tk.IntVar(value=0)
#前景色
foreColor = '#000000'
backColor = '#FFFFFF'
#创建画布
#记录最后绘制图形的id
lastDraw = 0
end=[0]  #每次抬起鼠标时，最后一组图形的编号
size="20"  #初始字号
#保存画布
def getter(widget):  #参数是画布的实体
    time.sleep(0.5)  #等待一会，否则会把点击“保存”那一刻也存进去
    x=top.winfo_x()+widget.winfo_x()  #不知道为什么会有偏差，所以进行了微调，扩大了截图范围
    y=top.winfo_y()+widget.winfo_y()
    if top.winfo_x()<0:  #获取的位置有问题，有可能为负数
        x=0
    if top.winfo_y()<0:
        y=0    
    x1=x+widget.winfo_width()+200
    y1=y+widget.winfo_height()+200
    filename=tk.filedialog.asksaveasfilename(filetypes=[('.jpg','JPG')],initialdir='C:\\Users\\lin042\\Desktop\\')    
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)

#鼠标左键单击，允许画图
def onLeftButtonDown(event):
    yesno.set(1)
    X.set(event.x)
    Y.set(event.y)
    if what.get()==4:
        canvas.create_text(event.x, event.y, font=("微软雅黑", int(size)),text=text,fill=foreColor)
        what.set(1)

#按住鼠标左键移动，画图
def onLeftButtonMove(event):
    global lastDraw
    if yesno.get()==0:
        return
    if what.get()==1:
        #使用当前选择的前景色绘制曲线
        lastDraw=canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)  #返回值就是对图形的计数，直接delete这个数字就能删除该图形
        X.set(event.x)
        Y.set(event.y)
    elif what.get()==2:
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        #绘制直线，先删除刚刚画过的直线，再画一条新的直线
        lastDraw=canvas.create_line(X.get(), Y.get(), event.x, event.y,
                                      fill=foreColor)
    elif what.get()==3:
        #绘制矩形，先删除刚刚画过的矩形，再画一个新的矩形
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw=canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,
                                            outline=foreColor)
                              
    elif what.get()==5:
        #橡皮，使用背景色填充10*10的矩形区域
        lastDraw=canvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5,
                                outline=backColor)
    elif what.get()==6:
        #绘制圆形，先删除刚刚画过的矩形，再画一个新的矩形
        try:
            canvas.delete(lastDraw)
        except Exception as e:
            pass
        lastDraw=canvas.create_oval(X.get(), Y.get(), event.x, event.y,
                                           fill=backColor, outline=foreColor)

#鼠标左键抬起，不允许画图
def onLeftButtonUp(event):
    global lastDraw
    if what.get()==2:
        #绘制直线
        
        lastDraw=canvas.create_line(X.get(), Y.get(), event.x, event.y, fill=foreColor)
    elif what.get()==3:

        lastDraw=canvas.create_rectangle(X.get(), Y.get(), event.x, event.y,  outline=foreColor)
    elif what.get()==6:

        lastDraw=canvas.create_oval ( X.get(), Y.get(), event.x, event.y,  outline=foreColor)
    yesno.set(0)
    end.append(lastDraw)

#鼠标右键抬起，弹出菜单
def onRightButtonUp(event):
    menu.post(event.x_root, event.y_root)



top.mainloop()
