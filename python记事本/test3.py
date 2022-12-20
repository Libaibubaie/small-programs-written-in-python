import tkinter as tk
# 创建一个窗口，作为我们程序的主窗口
win = tk.Tk()
# 创建画布
canvas = tk.Canvas(win)
canvas.pack()
# 程序陷入循环，等待操作
win.mainloop()
