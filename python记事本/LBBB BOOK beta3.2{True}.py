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
import pickle
import time
import math
import time
import os
numstrlist=[]#存储数字 符号
isjisuan=False#运算标志

def close_win():
    top.destroy()
    
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
        clock.place(x=588, y=1)
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
    print("(这只是一个简单的帮助)由于tk部分指令在3.8下无法正常调用，所以撤销和重做暂时实现不了，尝试修复后无果，为了保证代码的完整性，我们将会保留他们，但请你知道，它们没有任何用处(这是计划的一部分)")



def author():
    showinfo(title="作者", message="Libaibubai_official(Libaibubai@163.com)")


def power():
    showinfo(title="版权信息", message="Libaibubai_official")

def another():
    showinfo(title="作者的话", message="给程序以生命，而不是给生命以程序！")



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
            top.title("记事本")
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
        top.title("LBBB BOOK X")





top = tk.Tk()
top.title('LBBB Book beta3.2{True}')
top.geometry('800x600')
menu = tk.Menu(top,tearoff=True)


# 文件功能
filemenu = tk.Menu(menu)
filemenu.add_command(label="新建", accelerator="Ctrl+N", command=new_file)
filemenu.add_command(label="打开", accelerator="Ctrl+O", command=open_file)
filemenu.add_command(label="保存", accelerator="Ctrl+S", command=save)
filemenu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=save_as)
filemenu.add_command(label="重命名", accelerator="Ctrl+R", command=rename_file)
filemenu.add_command(label="删除", accelerator="Ctrl+D", command=delete)
filemenu.add_command(label="结束程序", accelerator="NONE", command=close_win)
menu.add_cascade(label="文件(第一目录)", menu=filemenu)

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
status_str_var = tk.StringVar()
status_str_var.set('LBBB BOOK beta 3.1 cslive Menu:{}'.format(278))
status_label = tk.Label(top,textvariable=status_str_var,bd=1,relief=tk.SUNKEN,anchor=tk.W)
status_label.pack(side=tk.BOTTOM,fill=tk.X)

var_line = tk.StringVar()
line_label = tk.Label(top,textvariable=var_line,width=1,relief=tk.SUNKEN,bg='#faebd7',anchor=tk.N,font=18)
line_label.pack(side=tk.LEFT,fill=tk.Y)


textPad = tk.Text(top,font=5)
textPad.pack(fill=tk.BOTH,expand=True)


scrollY = tk.Scrollbar(textPad)
textPad.config(yscrollcommand=scrollY.set)
scrollY.config(command=textPad.yview)
scrollY.pack(side=tk.RIGHT,fill=tk.Y)

scrollBarx =Scrollbar(top, orient=HORIZONTAL)
scrollBarx.pack(side=BOTTOM,fill=X)


# 关于功能
aboutmenu = tk.Menu(top)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="版权", command=power)
aboutmenu.add_command(label="作者的话", command=another)
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


#tkinter.colorchooser.askcolor()[1]
#def center_window(top,w, h):
    # 获取屏幕 宽、高
    #ws = app.winfo_screenwidth()
    #hs = app.winfo_screenheight()
    #app.geometry('%dx%d' % (w, h))
    
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
image = tk.PhotoImage()
canvas = tk.Canvas(top, bg='white', width=1, height=10)
canvas.create_image(1, 1, image=image)
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

canvas.bind('<Button-1>', onLeftButtonDown)  #单击左键
canvas.bind('<B1-Motion>', onLeftButtonMove)  #按住并移动左键
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)  #释放左键
canvas.bind('<ButtonRelease-3>', onRightButtonUp) #释放右键
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
#添加菜单，清除
def Clear():
    global lastDraw,end
    for item in canvas.find_all():
        canvas.delete(item)
    end=[0]
    lastDraw=0
menu.add_command(label='清屏', command=Clear)
#撤销
def Back():
    global end
    try:
        for i in range(end[-2],end[-1]+1): #要包含最后一个点，否则无法删除图形
                canvas.delete(i)
        end.pop()  #弹出末尾元素
    except:
        end=[0]
menu.add_command(label='撤销', command=Back)
#保存
def Save():
    getter(canvas)
menu.add_command(label='保存', command=Save)
menu.add_separator()  #添加分割线

'''子菜单及其关联的函数'''
menuType = tk.Menu(menu, tearoff=0)
def drawCurve():
    what.set(1)
menuType.add_command(label='铅笔',command=drawCurve)
def drawLine():
    what.set(2)
menuType.add_command(label='直线',command=drawLine)
def drawRectangle():
    what.set(3)
menuType.add_command(label='矩形',command=drawRectangle)
def drawCircle():
    what.set(6)
menuType.add_command(label='圆形',command=drawCircle)

#文本框
def drawText():
    global text,size
    text = tk.simpledialog.askstring(title='输入文本', prompt='')
    if text != None:
        size = tk.simpledialog.askinteger('输入字号',prompt='', initialvalue=20)  #默认值为20
        if size == None:
            size = "20"		
    what.set(4)
menuType.add_command(label='文本', command=drawText)
menuType.add_separator()
#选择前景色
def chooseForeColor():
    global foreColor
    foreColor = tk.colorchooser.askcolor()[1]
menuType.add_command(label='选择前景色', command=chooseForeColor)
#选择背景色

#橡皮
def onErase():
    what.set(5)
menuType.add_command(label='橡皮擦', command=onErase)
menu.add_cascade(label=' 工具栏', menu=menuType)

scrollZ = tk.Scrollbar(canvas)
canvas.config(yscrollcommand=scrollY.set)
scrollZ.config(command=canvas.yview)
scrollZ.pack(side=tk.RIGHT,fill=tk.Y)

filemenu = tk.Menu(menu)
filemenu.add_command(label="清屏", accelerator="Ctrl+Q", command=Clear)
menu.add_cascade(label=" 文件(第二目录)", menu=filemenu)

top.mainloop()
