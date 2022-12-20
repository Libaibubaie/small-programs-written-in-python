from tkinter import *
from tkinter import scrolledtext
from threading import Thread, RLock


class Main(Tk):
    def __init__(self):
        super().__init__()
        self.thread_lock = RLock()
        self.txt = ""
        self._main()

    def _main(self):
        self.resizable(True, True)
        self.geometry("800x600")
        self.edit_frame = Canvas(self, height=600, width=800,
                                 bg="white", highlightthickness=0)
        self.edit_frame.pack()
        self.line_text = Text(self.edit_frame, width=7, height=600, spacing3=5,
                              bg="#DCDCDC", bd=0, font=("等线等线 (Light)", 14), takefocus=0, state="disabled",
                              cursor="arrow")
        self.line_text.pack(side="left", expand="no")
        self.update()
        self.edit_text = scrolledtext.ScrolledText(self.edit_frame, height=1, wrap="none", spacing3=5,
                                                   width=self.winfo_width() - self.line_text.winfo_width(), bg="white",
                                                   bd=0, font=("等线等线 (Light)", 14), undo=True, insertwidth=1)
        self.edit_text.vbar.configure(command=self.scroll)
        self.edit_text.pack(side="left", fill="both")
        self.line_text.bind("<MouseWheel>", self.wheel)
        self.edit_text.bind("<MouseWheel>", self.wheel)
        self.edit_text.bind("<Control-v>", lambda e: self.get_txt_thread())
        self.edit_text.bind("<Control-V>", lambda e: self.get_txt_thread())
        self.edit_text.bind("<Key>", lambda e: self.get_txt_thread())
        self.show_line()

    def wheel(self, event):
        self.line_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.edit_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    def scroll(self, *xy):
        self.line_text.yview(*xy)
        self.edit_text.yview(*xy)

    def get_txt_thread(self):
        Thread(target=self.get_txt).start()

    def get_txt(self):
        self.thread_lock.acquire()
        if self.txt != self.edit_text.get("1.0", "end")[:-1]:
            self.txt = self.edit_text.get("1.0", "end")[:-1]
            self.show_line()
        else:
            self.thread_lock.release()

    def show_line(self):
        sb_pos = self.edit_text.vbar.get()
        self.line_text.configure(state="normal")
        self.line_text.delete("1.0", "end")
        txt_arr = self.txt.split("\n")
        if len(txt_arr) == 1:
            self.line_text.insert("1.1", " 1")
        else:
            for i in range(1, len(txt_arr) + 1):
                self.line_text.insert("end", " " + str(i))
                if i != len(txt_arr):
                    self.line_text.insert("end", "\n")
        if len(sb_pos) == 4:
            self.line_text.yview_moveto(0.0)
        elif len(sb_pos) == 2:
            self.line_text.yview_moveto(sb_pos[0])
            self.edit_text.yview_moveto(sb_pos[0])
        self.line_text.configure(state="disabled")
        try:
            self.thread_lock.release()
        except RuntimeError:
            pass


if __name__ == "__main__":
    run = Main()
    run.mainloop()

