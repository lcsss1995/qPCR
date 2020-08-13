import tkinter as tk

class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('qPCR数据统计分析')
        self.root.geometry('500x750')

        face1(self.root)

class face1():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='green')
        #基准界面face1
        self.face1 = tk.Frame(self.master)
        self.face1.pack()
        btn = tk.Button(self.face1, text = 'trun face2', command=self.change)
        btn.pack()

    def change(self,):
        self.face1.destroy()
        face2(self.master)

class face2():
    def __init__(self, master):
        self.master = master
        self.master.config(bg='blue')
        self.face2 = tk.Frame(self.master)
        self.face2.pack()
        btn_back = tk.Button(self.face2, text = 'turn face1', command = self.back)
        btn_back.pack()

    def back(self):
        self.face2.destroy()
        face1(self.master)

if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
