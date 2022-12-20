import tkinter
import tkinter as tk
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog

import time


#tkinter.colorchooser.askcolor()[1]
def center_window(top,w, h):
    # 获取屏幕 宽、高
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    app.geometry('%dx%d' % (w, h))
    
app = tkinter.Tk()
app.title('我的画图')
center_window(app,800,600)
menu = tkinter.Menu(app, tearoff=0)
#控制是否允许画图的变量，1：允许，0：不允许
yesno = tkinter.IntVar(value=0)
#控制画图类型的变量，1：曲线，2：直线，3：矩形，4：文本，5：橡皮 6：圆形
what = tkinter.IntVar(value=1)
#记录鼠标位置的变量
X = tkinter.IntVar(value=0)
Y = tkinter.IntVar(value=0)
#前景色
foreColor = '#000000'
backColor = '#FFFFFF'
#创建画布
image = tkinter.PhotoImage()
canvas = tkinter.Canvas(app, bg='white', width=800, height=600)
canvas.create_image(800, 600, image=image)
#记录最后绘制图形的id
lastDraw = 0
end=[0]  #每次抬起鼠标时，最后一组图形的编号
size="20"  #初始字号
#保存画布
def getter(widget):  #参数是画布的实体
    time.sleep(0.5)  #等待一会，否则会把点击“保存”那一刻也存进去
    x=app.winfo_x()+widget.winfo_x()  #不知道为什么会有偏差，所以进行了微调，扩大了截图范围
    y=app.winfo_y()+widget.winfo_y()
    if app.winfo_x()<0:  #获取的位置有问题，有可能为负数
        x=0
    if app.winfo_y()<0:
        y=0    
    x1=x+widget.winfo_width()+200
    y1=y+widget.winfo_height()+200
    filename=tkinter.filedialog.asksaveasfilename(filetypes=[('.jpg','JPG')],initialdir='C:\\Users\\lin042\\Desktop\\')    
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
