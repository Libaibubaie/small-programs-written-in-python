import os
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title('04 记事本')
root.geometry("800x500+100+100")
"""记事本事件 1"""
filename = ""


def new_file():
    """新建文件"""
    global filename
    root.title('未命名文件')
    filename = None
    textPad.delete(1.0, tk.END)


def open_file():
    """打开已经存在的文件"""
    global filename
    filename = filedialog.askopenfilename()
    if filename == '':
        filename = None
    else:
        root.title('FileName:' + os.path.basename(filename))
        textPad.delete(1.0, tk.END)
        text = open(filename, 'r', encoding='utf-8').read()
        textPad.insert(1.0, text)


def save_as():
    global filename
    filename = filedialog.asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    open(filename, 'w').write(textPad.get(1.0, tk.END))
    root.title('FileName:' + os.path.basename(filename))


def author():
    messagebox.showinfo('作者信息', '本软件有青灯教育正心老师编写')


def about():
    messagebox.showinfo('版权信息.Copyleft', '本软件版权归属为青灯教育')


"""记事本布局"""
"""创建菜单栏"""
menubar = tk.Menu(root, tearoff=False)
root.config(menu=menubar)

"""创建二级菜单 文件"""
file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label='新建')
file_menu.add_command(label='打开', command=open_file)
file_menu.add_command(label='保存')
file_menu.add_command(label='另存为', command=save_as)
# 设置二级菜单的名字
menubar.add_cascade(label='文件', menu=file_menu)

"""创建二级菜单 编辑"""
edit_menu = tk.Menu(menubar, tearoff=False)
edit_menu.add_command(label='撤销')
edit_menu.add_command(label='重做')
# 添加分割线
edit_menu.add_separator()
edit_menu.add_command(label="复制")
edit_menu.add_command(label="剪切")
edit_menu.add_command(label="粘贴")
menubar.add_cascade(label="编辑", menu=edit_menu)

"""创建二级菜单 关于"""
about_menu = tk.Menu(menubar, tearoff=False)
about_menu.add_command(label="作者", command=author)
about_menu.add_command(label="版权", command=about)
menubar.add_cascade(label="关于", menu=about_menu)

var_status = tk.StringVar()
var_format = "字符数：{}"
var_status.set(var_format.format(0))
# 状态栏
status = tk.Label(root, textvariable=var_status, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

var_line = tk.StringVar()
# 行数
line_label = tk.Label(root, width=1, bg='antique white', textvariable=var_line, anchor=tk.N, font=18)
line_label.pack(side=tk.LEFT, fill=tk.Y)

# 文本编辑区域
textPad = tk.Text(root, undo=True, font=18)
textPad.pack(expand=tk.YES, fill=tk.BOTH)



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

if __name__ == '__main__':
    root.mainloop()
