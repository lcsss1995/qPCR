#qPCR_V4
import tkinter as tk
import numpy as np
import tkinter.messagebox
import base64
import os
from one_png import img as one
from two_png import img as two

class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.title('qPCR数据统计分析_V4 for lcsss')
        self.root.geometry('500x750')
        
        face1(self.root)
        

class face1():
    def __init__(self, master):
        self.master = master
        #基准界面无实验组的为face1
        self.face1 = tk.Frame(self.master,width=500,height=800)
        self.face1.place(x=0, y=0)
        #photo
        self.canvas = tk.Canvas(self.face1, height=500,width=500)
        tmp = open('one.png', 'wb')
        tmp.write(base64.b64decode(one))
        tmp.close()
        self.image_file = tk.PhotoImage(file='one.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.place(x=0, y=0)
                                    
        btn_change = tk.Button(self.face1, text = 'trun face2', command=self.change,width=8, height=2)
        btn_change.place(x=210, y=690)
        btn_input = tk.Button(self.face1, text='input', command=self.usr_input1, width=8, height=2)
        btn_input.place(x=90, y=690)
        btn_help = tk.Button(self.face1, text='help', command=self.usr_help1,width=8, height=2)
        btn_help.place(x=330, y=690)
        
        #input information
        tk.Label(self.face1, text='无对照组模式').place(x=200, y=510)
        tk.Label(self.face1, text='reference gene').place(x=0, y=555)
        tk.Label(self.face1, text='reference gene').place(x=0, y=590)
        tk.Label(self.face1, text='reference gene').place(x=0, y=625)
        tk.Label(self.face1, text='target gene').place(x=250, y=555)
        tk.Label(self.face1, text='target gene').place(x=250, y=590)
        tk.Label(self.face1, text='target gene').place(x=250, y=625)
        self.r_gene_1 = tk.StringVar()
        self.r_gene_2 = tk.StringVar()
        self.r_gene_3 = tk.StringVar()
        self.t_gene_1 = tk.StringVar()
        self.t_gene_2 = tk.StringVar()
        self.t_gene_3 = tk.StringVar()
        entry_er1 = tk.Entry(self.face1, textvariable=self.r_gene_1)
        entry_er1.place(x=100, y=555)
        entry_er2 = tk.Entry(self.face1, textvariable=self.r_gene_2)
        entry_er2.place(x=100, y=590)
        entry_er3 = tk.Entry(self.face1, textvariable=self.r_gene_3)
        entry_er3.place(x=100, y=625)
        entry_tr1 = tk.Entry(self.face1, textvariable=self.t_gene_1)
        entry_tr1.place(x=350, y=555)
        entry_tr2 = tk.Entry(self.face1, textvariable=self.t_gene_2)
        entry_tr2.place(x=350, y=590)
        entry_tr3 = tk.Entry(self.face1, textvariable=self.t_gene_3)
        entry_tr3.place(x=350, y=625)

    def usr_input1(self):
        r1 = self.r_gene_1.get()
        r2 = self.r_gene_2.get()
        r3 = self.r_gene_3.get()
        t1 = self.t_gene_1.get()
        t2 = self.t_gene_2.get()
        t3 = self.t_gene_3.get()
        r = np.array([r1, r2, r3], dtype = float)
        t = np.array([t1, t2, t3], dtype = float)
        m_r = np.mean(r)
        dv = m_r -t
        Ct1 = np.power(2, dv)
        m_Ct1 = np.mean(Ct1)
        std_Ct1 = np.std(Ct1)
        cv_Ct1 = std_Ct1/m_Ct1
        tk.messagebox.showinfo(title = '分析结果', message = '目的基因的表达量为内参基因的{:.2f}%,标准差为{:.2f},CV值为{:.2f}'.format(m_Ct1*100, std_Ct1, cv_Ct1))

    def usr_help1(self):
        tk.messagebox.showinfo(title = 'help', message = 'face1：无对照组qPCR，face2：有对照组qPCR。统计方法使用比较Ct方法（2-△△Ct），在对应框内输入对应CT值，点击input即可，有建议请联系wx：327109739。')
    
    def change(self):
        self.face1.destroy()
        face2(self.master)

class face2():
    def __init__(self, master):
        self.master = master
        #基准界面有实验组的为face2
        self.face2 = tk.Frame(self.master,width=500,height=800)
        self.face2.place(x=0, y=0)
        #photo
        self.canvas = tk.Canvas(self.face2, height=500,width=500)
        tmp = open('two.png', 'wb')
        tmp.write(base64.b64decode(two))
        tmp.close()
        self.image_file = tk.PhotoImage(file='two.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.place(x=0,y=0)
        
        btn_back = tk.Button(self.face2, text = 'turn face1', command = self.back,width=8, height=2)
        btn_back.place(x=210, y= 690)
        btn_input = tk.Button(self.face2, text='input', command=self.usr_input2, width=8, height=2)
        btn_input.place(x=90, y=690)
        btn_help = tk.Button(self.face2, text='help', command=self.usr_help2,width=8, height=2)
        btn_help.place(x=330, y=690)

        #input information
        tk.Label(self.face2, text='实验组').place(x=100, y=500)
        tk.Label(self.face2, text='对照组').place(x=300, y=500)
        tk.Label(self.face2, text='reference gene').place(x=0, y=525)
        tk.Label(self.face2, text='reference gene').place(x=0, y=550)
        tk.Label(self.face2, text='reference gene').place(x=0, y=575)
        tk.Label(self.face2, text='reference gene').place(x=250, y=525)
        tk.Label(self.face2, text='reference gene').place(x=250, y=550)
        tk.Label(self.face2, text='reference gene').place(x=250, y=575)
        tk.Label(self.face2, text='target gene').place(x=0, y=600)
        tk.Label(self.face2, text='target gene').place(x=0, y=625)
        tk.Label(self.face2, text='target gene').place(x=0, y=650)
        tk.Label(self.face2, text='target gene').place(x=250, y=600)
        tk.Label(self.face2, text='target gene').place(x=250, y=625)
        tk.Label(self.face2, text='target gene').place(x=250, y=650)
        

        self.e_r_gene_1 = tk.StringVar()
        self.e_r_gene_2 = tk.StringVar()
        self.e_r_gene_3 = tk.StringVar()
        self.e_t_gene_1 = tk.StringVar()
        self.e_t_gene_2 = tk.StringVar()
        self.e_t_gene_3 = tk.StringVar()
        entry_er1 = tk.Entry(self.face2, textvariable=self.e_r_gene_1)
        entry_er1.place(x=100, y=525)
        entry_er2 = tk.Entry(self.face2, textvariable=self.e_r_gene_2)
        entry_er2.place(x=100, y=550)
        entry_er3 = tk.Entry(self.face2, textvariable=self.e_r_gene_3)
        entry_er3.place(x=100, y=575)
        entry_tr1 = tk.Entry(self.face2, textvariable=self.e_t_gene_1)
        entry_tr1.place(x=100, y=600)
        entry_tr2 = tk.Entry(self.face2, textvariable=self.e_t_gene_2)
        entry_tr2.place(x=100, y=625)
        entry_tr3 = tk.Entry(self.face2, textvariable=self.e_t_gene_3)
        entry_tr3.place(x=100, y=650)

        self.c_r_gene_1 = tk.StringVar()
        self.c_r_gene_2 = tk.StringVar()
        self.c_r_gene_3 = tk.StringVar()
        self.c_t_gene_1 = tk.StringVar()
        self.c_t_gene_2 = tk.StringVar()
        self.c_t_gene_3 = tk.StringVar()
        entry_er1 = tk.Entry(self.face2, textvariable=self.c_r_gene_1)
        entry_er1.place(x=350, y=525)
        entry_er2 = tk.Entry(self.face2, textvariable=self.c_r_gene_2)
        entry_er2.place(x=350, y=550)
        entry_er3 = tk.Entry(self.face2, textvariable=self.c_r_gene_3)
        entry_er3.place(x=350, y=575)
        entry_tr1 = tk.Entry(self.face2, textvariable=self.c_t_gene_1)
        entry_tr1.place(x=350, y=600)
        entry_tr2 = tk.Entry(self.face2, textvariable=self.c_t_gene_2)
        entry_tr2.place(x=350, y=625)
        entry_tr3 = tk.Entry(self.face2, textvariable=self.c_t_gene_3)
        entry_tr3.place(x=350, y=650)

    def usr_input2(self):
        er1 = self.e_r_gene_1.get()
        er2 = self.e_r_gene_2.get()
        er3 = self.e_r_gene_3.get()
        et1 = self.e_t_gene_1.get()
        et2 = self.e_t_gene_2.get()
        et3 = self.e_t_gene_3.get()
        cr1 = self.c_r_gene_1.get()
        cr2 = self.c_r_gene_2.get()
        cr3 = self.c_r_gene_3.get()
        ct1 = self.c_t_gene_1.get()
        ct2 = self.c_t_gene_2.get()
        ct3 = self.c_t_gene_3.get()
        e_r = np.array([er1, er2, er3], dtype = float)
        e_t = np.array([et1, et2, et3], dtype = float)
        c_r = np.array([cr1, cr2, cr3], dtype = float)
        c_t = np.array([ct1, ct2, ct3], dtype = float)
        e_dv = e_t - e_r
        c_dv = c_t - c_r
        e_Ct1 = np.power(2, -e_dv)
        c_Ct1 = np.power(2, -c_dv)
        m_c_Ct1 = np.mean(c_Ct1)
        e_Ct2 = e_Ct1/m_c_Ct1
        c_Ct2 = c_Ct1/m_c_Ct1
        e_fc = np.mean(e_Ct2)
        c_fc = np.mean(c_Ct2)
        e_std = np.std(e_Ct2, ddof=1)
        c_std = np.std(c_Ct2, ddof=1)
        e_cv = e_std/e_fc
        c_cv = c_std/c_fc
        tk.messagebox.showinfo(title = '分析结果', message = '实验组目的基因的相对表达量为{:.2f},标准差为{:.2f},CV值为{:.4f}对照组目的基因的相对表达量为{:.2f},标准差为{:.2f},CV值为{:.2f}'.format(e_fc, e_std, e_cv, c_fc, c_std, c_cv))

    def usr_help2(self):
        tk.messagebox.showinfo(title = 'help', message = '统计方法使用比较Ct方法（2-△△Ct），设计实验中实验组和对照组至少要有3个生物学重复来检测某目的基因（target，设定内参基因为reference）,在对应框内输入对应CT值，点击input即可。若有建议请联系wx：327109739')
       

    def back(self):
        self.face2.destroy()
        face1(self.master)

    

if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
