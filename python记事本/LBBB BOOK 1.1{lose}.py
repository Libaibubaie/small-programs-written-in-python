#画图软件的实现
from tkinter.filedialog import *
from tkinter import *
from tkinter.colorchooser import *
 
win_width=900
win_height=450
 
 
class Application(Frame):
  def __init__(self,master=None,bgcolor="#000000"):
 
    super().__init__(master)
    self.master=master
    self.bgcolor=bgcolor
    self.x=0
    self.y=0
    self.fgcolor="#ff0000"
    self.lastDraw=0 #表示最后绘制的图形的id
    self.startDrawFlag=False
    self.pack()
def createWidget(self):
  # 创建画板
  self.drawCad=Canvas(self,width=win_width,height=win_height*0.9,bg=self.bgcolor)
  self.drawCad.pack()
  # 创建按钮
  btn_start = Button(self,text="开始",name="start")
  btn_start.pack(side="left",padx=10)
  btn_pen = Button(self, text="画笔", name="pen")
  btn_pen.pack(side="left", padx=10)
  btn_rect = Button(self, text="矩形", name="rect")
  btn_rect.pack(side="left", padx=10)
  btn_clear = Button(self, text="清屏", name="clear")
  btn_clear.pack(side="left", padx=10)
  btn_earsor = Button(self, text="橡皮擦", name="earsor")
  btn_earsor.pack(side="left", padx=10)
  btn_line = Button(self, text="直线", name="line")
  btn_line.pack(side="left", padx=10)
  btn_lineArrow = Button(self, text="箭头直线", name="lineArrow")
  btn_lineArrow.pack(side="left", padx=10)
  btn_color = Button(self, text="颜色", name="color")
  btn_color.pack(side="left", padx=10)
  #为按钮绑定事件
  btn_pen.bind_class("Button","<1>",self.eventManger)
  self.drawCad.bind("<ButtonRelease-1>",self.stopDraw)
def eventManger(self,event):
  name=event.widget.winfo_name()
  print(name)
  if name=="line" :
    self.drawCad.bind("<B1-Motion>",self.myline)
  elif name=="lineArrow":
    self.drawCad.bind("<B1-Motion>", self.mylineArrow)
  elif name=="rect":
    self.drawCad.bind("<B1-Motion>", self.myRect)
  elif name=="pen":
    self.drawCad.bind("<B1-Motion>", self.myPen)
  elif name=="earsor":
    self.drawCad.bind("<B1-Motion>", self.myEarsor)
  elif name=="clear":
    self.drawCad.delete("all")
  elif name=="color":
   c= askcolor(color=self.fgcolor,title="画笔选择颜色")
   self.fgcolor=c[1]
 
def myline(self,event):
  self.startDraw(event)
  self.lastDraw=self.drawCad.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)
 
def mylineArrow(self,event):
  self.startDraw(event)
  self.lastDraw = self.drawCad.create_line(self.x, self.y, event.x, event.y,arrow=LAST , fill=self.fgcolor)
 
def myRect(self,event):
  self.startDraw(event)
  self.lastDraw = self.drawCad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)
 
def myPen(self,event):
  self.startDraw(event)
  self.drawCad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)
  self.x=event.x
  self.y=event.y
def myEarsor(self,event):
  self.startDraw(event)
  self.drawCad.create_rectangle(event.x-4, event.y-4, event.x+4, event.y+4, fill=self.bgcolor)
  self.x = event.x
  self.y = event.y
def stopDraw(self,event):
  self.startDrawFlag=False
  self.lastDraw=0
 
def startDraw(self,event):
  self.drawCad.delete(self.lastDraw)
  if not self.startDrawFlag:
    self.startDrawFlag = True
    self.x = event.x
    self.y = event.y
root=Tk()
app=Application(root)
root.geometry(str(win_width)+"x"+str(win_height)+"+100+100")
root.mainloop()
