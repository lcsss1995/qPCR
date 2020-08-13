#qPCR_V5
import tkinter as tk
import numpy as np
import tkinter.messagebox
import base64
import os
import xlrd
import xlwt
from one_png import img as one
from two_png import img as two
from tkinter import filedialog


class basedesk():
    def __init__(self, master):
        self.root = master
        self.root.title('qPCR数据统计分析_V5 for wx:327109739')
        self.root.geometry('500x750')
        
        face2(self.root)
        

class face1():
    def __init__(self, master):
        self.master = master
        #基准界面无实验组的为face1
        self.face1 = tk.Frame(self.master,width=500,height=750)
        self.face1.place(x=0, y=0)
        #photo
        self.canvas = tk.Canvas(self.face1, height=500,width=500)
        tmp = open('one.png', 'wb')
        tmp.write(base64.b64decode(one))
        tmp.close()
        self.image_file = tk.PhotoImage(file='one.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.place(x=0, y=0)
        #按钮
        btn_input = tk.Button(self.face1, text='运行', command=self.usr_input1, width=10, height=2)
        btn_input.place(x=25, y=690)
        btn_change = tk.Button(self.face1, text = '对照组模式', command=self.usr_change,width=10, height=2)
        btn_change.place(x=275, y=690)
        btn_change = tk.Button(self.face1, text = '一键导入数据', command=self.usr_import,width=10, height=2)
        btn_change.place(x=150, y=690)
        btn_help = tk.Button(self.face1, text='帮助', command=self.usr_help1,width=10, height=2)
        btn_help.place(x=400, y=690)
        
        #input information
        tk.Label(self.face1, text='无对照组模式', font = 20).place(x=210, y=500)
        tk.Label(self.face1, text='reference gene', font = 20).place(x=85, y=520)
        tk.Label(self.face1, text='target gene',font = 20).place(x=335, y=520)
        self.r_gene_1 = tk.StringVar()
        self.r_gene_2 = tk.StringVar()
        self.r_gene_3 = tk.StringVar()
        self.t_gene_1 = tk.StringVar()
        self.t_gene_2 = tk.StringVar()
        self.t_gene_3 = tk.StringVar()
        entry_er1 = tk.Entry(self.face1, textvariable=self.r_gene_1)
        entry_er1.place(x=15, y=550, width=230, height=35)
        entry_er2 = tk.Entry(self.face1, textvariable=self.r_gene_2)
        entry_er2.place(x=15, y=595, width=230, height=35)
        entry_er3 = tk.Entry(self.face1, textvariable=self.r_gene_3)
        entry_er3.place(x=15, y=635, width=230, height=35)
        entry_tr1 = tk.Entry(self.face1, textvariable=self.t_gene_1)
        entry_tr1.place(x=255, y=550, width=230, height=35)
        entry_tr2 = tk.Entry(self.face1, textvariable=self.t_gene_2)
        entry_tr2.place(x=255, y=595, width=230, height=35)
        entry_tr3 = tk.Entry(self.face1, textvariable=self.t_gene_3)
        entry_tr3.place(x=255, y=635, width=230, height=35)

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
        std_Ct1 = np.std(Ct1, ddof=1)
        cv_Ct1 = std_Ct1/m_Ct1
        tk.messagebox.showinfo(title = '分析结果', message = '目的基因的表达量为内参基因的{:.2f}%,\n标准差为{:.2f},\nCV值为{:.2f}'.format(m_Ct1*100, std_Ct1, cv_Ct1))

    def usr_help1(self):
        tk.messagebox.showinfo(title = 'help', message = '使用前请先看文件夹内的 readme, 希望能得到你积极的反馈')

    def usr_change(self):
        self.face1.destroy()
        face2(self.master)

    def usr_import(self):
        #excel读取
        Filepath = filedialog.askopenfilename()
        excel = xlrd.open_workbook(Filepath)
        table = excel.sheets()[0]
        ncols = table.ncols
        r_gene = []
        t_gene = []
        for i in range(ncols):
            r_gene.append(table.col_values(i)[1:4])
            t_gene.append(table.col_values(i)[4:])
        #数据处理
        i_r = np.array(r_gene,dtype = float)
        i_t = np.array(t_gene,dtype = float)
        m_i_r = np.mean(i_r, axis = 1)
        i_dv = []
        for i in range(0, ncols):
            i_dv.append(m_i_r[i]-i_t[i])
        i_dv = np.array(i_dv)
        i_Ct1 = np.power(2, i_dv)
        m_i_Ct1 = np.mean(i_Ct1, axis = 1)
        std_i_Ct1 = np.std(i_Ct1, ddof=1, axis = 1)
        cv_i_Ct1 =std_i_Ct1/m_i_Ct1
        #excel写出
        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet('result')
        worksheet.write(1, 0, label = '相对表达量')
        worksheet.write(2, 0, label = '标准差')
        worksheet.write(3, 0, label = 'CV值')
        for i in range (0,ncols):
            worksheet.write(0, i+1, i+1)
            worksheet.write(1, i+1, m_i_Ct1[i])
            worksheet.write(2, i+1, std_i_Ct1[i])
            worksheet.write(3, i+1, cv_i_Ct1[i])
        workbook.save('result.xls')
        
class face2():
    def __init__(self, master):
        self.master = master
        #基准界面有实验组的为face2
        self.face2 = tk.Frame(self.master,width=500,height=750)
        self.face2.place(x=0, y=0)
        #photo
        self.canvas = tk.Canvas(self.face2, height=500,width=500)
        tmp = open('two.png', 'wb')
        tmp.write(base64.b64decode(two))
        tmp.close()
        self.image_file = tk.PhotoImage(file='two.png')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.place(x=0,y=0)
        
        btn_back = tk.Button(self.face2, text = '无对照模式', command = self.back, width=10, height=2)
        btn_back.place(x=275, y= 690)
        btn_input = tk.Button(self.face2, text='运行', command=self.usr_input2, width=10, height=2)
        btn_input.place(x=25, y=690)
        btn_help = tk.Button(self.face2, text='帮助', command=self.usr_help2, width=10, height=2)
        btn_help.place(x=400, y=690)
        btn_change = tk.Button(self.face2, text = '一键导入数据', command=self.usr_import2,width=10, height=2)
        btn_change.place(x=150, y=690)

        #input information
        tk.Label(self.face2, text='实验组', font = 20).place(x=100, y=500)
        tk.Label(self.face2, text='对照组', font = 20).place(x=300, y=500)
        tk.Label(self.face2, text=' reference\ngene    ', font = 20).place(x=0, y=525)
        tk.Label(self.face2, text=' reference\ngene    ', font = 20).place(x=250, y=525)
        tk.Label(self.face2, text=' target\ngene ', font = 20).place(x=0, y=610)
        tk.Label(self.face2, text=' target\ngene ', font = 20).place(x=250, y=610)
        

        self.e_r_gene_1 = tk.StringVar()
        self.e_r_gene_2 = tk.StringVar()
        self.e_r_gene_3 = tk.StringVar()
        self.e_t_gene_1 = tk.StringVar()
        self.e_t_gene_2 = tk.StringVar()
        self.e_t_gene_3 = tk.StringVar()
        entry_er1 = tk.Entry(self.face2, textvariable=self.e_r_gene_1)
        entry_er1.place(x=90, y=525)
        entry_er2 = tk.Entry(self.face2, textvariable=self.e_r_gene_2)
        entry_er2.place(x=90, y=550)
        entry_er3 = tk.Entry(self.face2, textvariable=self.e_r_gene_3)
        entry_er3.place(x=90, y=575)
        entry_tr1 = tk.Entry(self.face2, textvariable=self.e_t_gene_1)
        entry_tr1.place(x=90, y=610)
        entry_tr2 = tk.Entry(self.face2, textvariable=self.e_t_gene_2)
        entry_tr2.place(x=90, y=635)
        entry_tr3 = tk.Entry(self.face2, textvariable=self.e_t_gene_3)
        entry_tr3.place(x=90, y=660)

        self.c_r_gene_1 = tk.StringVar()
        self.c_r_gene_2 = tk.StringVar()
        self.c_r_gene_3 = tk.StringVar()
        self.c_t_gene_1 = tk.StringVar()
        self.c_t_gene_2 = tk.StringVar()
        self.c_t_gene_3 = tk.StringVar()
        entry_er1 = tk.Entry(self.face2, textvariable=self.c_r_gene_1)
        entry_er1.place(x=340, y=525)
        entry_er2 = tk.Entry(self.face2, textvariable=self.c_r_gene_2)
        entry_er2.place(x=340, y=550)
        entry_er3 = tk.Entry(self.face2, textvariable=self.c_r_gene_3)
        entry_er3.place(x=340, y=575)
        entry_tr1 = tk.Entry(self.face2, textvariable=self.c_t_gene_1)
        entry_tr1.place(x=340, y=610)
        entry_tr2 = tk.Entry(self.face2, textvariable=self.c_t_gene_2)
        entry_tr2.place(x=340, y=635)
        entry_tr3 = tk.Entry(self.face2, textvariable=self.c_t_gene_3)
        entry_tr3.place(x=340, y=660)

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
        tk.messagebox.showinfo(title = '分析结果', message = '实验组目的基因的相对表达量为{:.2f},标准差为{:.2f},CV值为{:.4f}\n对照组目的基因的相对表达量为{:.2f},标准差为{:.2f},CV值为{:.2f}'.format(e_fc, e_std, e_cv, c_fc, c_std, c_cv))

    def usr_import2(self):
        #excel写入
        Filepath = filedialog.askopenfilename()
        excel = xlrd.open_workbook(Filepath)
        table = excel.sheets()[0]
        ncols = table.ncols
        e_r_gene = []
        e_t_gene = []
        c_r_gene = []
        c_t_gene = []
        for i in range(0, ncols):
            if i%2 == 0:
                e_t_gene.append(table.col_values(i)[3:6])
                c_t_gene.append(table.col_values(i)[9:12])
            else:
                e_r_gene.append(table.col_values(i)[3:6])
                c_r_gene.append(table.col_values(i)[9:12])
        #数据分析
        i_e_t = np.array(e_t_gene,dtype = float)
        i_e_r = np.array(e_r_gene,dtype = float)
        i_c_t = np.array(c_t_gene,dtype = float)
        i_c_r = np.array(c_r_gene,dtype = float)
        m_i_e_t = np.mean(i_e_t, axis=1)
        m_i_e_r = np.mean(i_e_r, axis=1)
        m_i_c_t = np.mean(i_c_t, axis=1)
        m_i_c_r = np.mean(i_c_r, axis=1)
        i_e_dv = m_i_e_t - m_i_e_r
        i_c_dv = m_i_c_t - m_i_c_r
        i_e_Ct1 = np.power(2, -i_e_dv)
        i_c_Ct1 = np.power(2, -i_c_dv)
        i_m_c_Ct1 = np.mean(i_c_Ct1)
        i_e_Ct2 = i_e_Ct1/i_m_c_Ct1
        i_c_Ct2 = i_c_Ct1/i_m_c_Ct1
        i_e_fc = np.mean(i_e_Ct2)
        i_c_fc = np.mean(i_c_Ct2)
        i_e_std = np.std(i_e_Ct2, ddof=1)
        i_c_std = np.std(i_c_Ct2, ddof=1)
        i_e_cv = i_e_std/i_e_fc
        i_c_cv = i_c_std/i_c_fc
        #excel写出
        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet('result')
        worksheet.write(0, 1, label = '目的基因')
        worksheet.write(0, 2, label = '内参基因')
        worksheet.write(1, 0, label = '相对表达量')
        worksheet.write(2, 0, label = '标准差')
        worksheet.write(3, 0, label = 'CV值')
        worksheet.write(1, 1, i_e_fc)
        worksheet.write(1, 2, i_c_fc)
        worksheet.write(2, 1, i_e_std)
        worksheet.write(2, 2, i_c_std)
        worksheet.write(3, 1, i_e_cv)
        worksheet.write(3, 2, i_c_cv)
        workbook.save('result.xls')
        
    def usr_help2(self):
        tk.messagebox.showinfo(title = 'help', message = '使用前请先看文件夹内的 readme, 希望能得到你积极的反馈')

    def back(self):
        self.face2.destroy()
        face1(self.master)

    

if __name__ == '__main__':
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
