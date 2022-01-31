"""测试一个经典的GUI程序的写法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.label01 = Label(self, text="fzy", width=10, height=2
                             , bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="fzy111", width=10, height=2
                             , bg="blue", fg="white", font=('黑体', 30))
        self.label02.pack()
        global photo
        photo = PhotoImage(file="img/1.png")
        self.label03 = Label(self, image=photo)
        self.label03.pack()
        self.label04 = Label(self, text="老范\n太帅了"
                             , borderwidth=5, relief="groove", justify="right")
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    root.title("一个经典的GUI程序")
    app = Application(master=root)
    root.mainloop()
