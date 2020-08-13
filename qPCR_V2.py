#qPCR_V1
import tkinter
import numpy as np
import tkinter.messagebox


window = tkinter.Tk()
window.title('qPCR数据统计分析V1--for 小罗')
window.geometry('500x750')

#image
canvas = tkinter.Canvas(window, height=500, width=2000)
image_file = tkinter.PhotoImage(file='C:/Users/lcsss/Pictures/Camera Roll/timg.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side = 'top')

#input information
tkinter.Label(window, text='实验组').place(x=100, y=500)
tkinter.Label(window, text='对照组').place(x=300, y=500)
tkinter.Label(window, text='reference gene').place(x=0, y=525)
tkinter.Label(window, text='reference gene').place(x=0, y=550)
tkinter.Label(window, text='reference gene').place(x=0, y=575)
tkinter.Label(window, text='reference gene').place(x=250, y=525)
tkinter.Label(window, text='reference gene').place(x=250, y=550)
tkinter.Label(window, text='reference gene').place(x=250, y=575)
tkinter.Label(window, text='target gene').place(x=0, y=600)
tkinter.Label(window, text='target gene').place(x=0, y=625)
tkinter.Label(window, text='target gene').place(x=0, y=650)
tkinter.Label(window, text='target gene').place(x=250, y=600)
tkinter.Label(window, text='target gene').place(x=250, y=625)
tkinter.Label(window, text='target gene').place(x=250, y=650)

e_r_gene_1 = tkinter.StringVar()
e_r_gene_2 = tkinter.StringVar()
e_r_gene_3 = tkinter.StringVar()
e_t_gene_1 = tkinter.StringVar()
e_t_gene_2 = tkinter.StringVar()
e_t_gene_3 = tkinter.StringVar()
entry_er1 = tkinter.Entry(window, textvariable=e_r_gene_1)
entry_er1.place(x=100, y=525)
entry_er2 = tkinter.Entry(window, textvariable=e_r_gene_2)
entry_er2.place(x=100, y=550)
entry_er3 = tkinter.Entry(window, textvariable=e_r_gene_3)
entry_er3.place(x=100, y=575)
entry_tr1 = tkinter.Entry(window, textvariable=e_t_gene_1)
entry_tr1.place(x=100, y=600)
entry_tr2 = tkinter.Entry(window, textvariable=e_t_gene_2)
entry_tr2.place(x=100, y=625)
entry_tr3 = tkinter.Entry(window, textvariable=e_t_gene_3)
entry_tr3.place(x=100, y=650)

c_r_gene_1 = tkinter.StringVar()
c_r_gene_2 = tkinter.StringVar()
c_r_gene_3 = tkinter.StringVar()
c_t_gene_1 = tkinter.StringVar()
c_t_gene_2 = tkinter.StringVar()
c_t_gene_3 = tkinter.StringVar()
entry_er1 = tkinter.Entry(window, textvariable=c_r_gene_1)
entry_er1.place(x=350, y=525)
entry_er2 = tkinter.Entry(window, textvariable=c_r_gene_2)
entry_er2.place(x=350, y=550)
entry_er3 = tkinter.Entry(window, textvariable=c_r_gene_3)
entry_er3.place(x=350, y=575)
entry_tr1 = tkinter.Entry(window, textvariable=c_t_gene_1)
entry_tr1.place(x=350, y=600)
entry_tr2 = tkinter.Entry(window, textvariable=c_t_gene_2)
entry_tr2.place(x=350, y=625)
entry_tr3 = tkinter.Entry(window, textvariable=c_t_gene_3)
entry_tr3.place(x=350, y=650)

def usr_input():
    er1 = e_r_gene_1.get()
    er2 = e_r_gene_2.get()
    er3 = e_r_gene_3.get()
    et1 = e_t_gene_1.get()
    et2 = e_t_gene_2.get()
    et3 = e_t_gene_3.get()
    cr1 = c_r_gene_1.get()
    cr2 = c_r_gene_2.get()
    cr3 = c_r_gene_3.get()
    ct1 = c_t_gene_1.get()
    ct2 = c_t_gene_2.get()
    ct3 = c_t_gene_3.get()
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
    #两者之间有一个区别：默认情况下，Excel会STDEV计算样本标准差，而NumPy会std计算总体标准差（行为类似于Excel STDEVP）。
    #为了使NumPy的std功能像Excel一样STDEV，请传递值ddof=1：
    e_std = np.std(e_Ct2, ddof=1)
    c_std = np.std(c_Ct2, ddof=1)
    e_cv = e_std/e_fc
    c_cv = c_std/c_fc
    tkinter.messagebox.showinfo(title = '分析结果', message = '实验组目的基因的相对表达量为{:.2f},标准差为{:.2f},CV值为{:.2f}\n对照组目的基因的相对表达量为{:.2f},标准差为{:.2f},CV值为{:.2f}'.format(e_fc, e_std, e_cv, c_fc, c_std, c_cv))

def usr_help():
    tkinter.messagebox.showinfo(title = 'help', message = '统计方法使用比较Ct方法（2-△△Ct），设计实验中实验组和对照组至少要有3个生物学重复，来检测某目的基因（target，设定内参基因为reference）,在框内输入对应CT值，点击input即可。若有建议请联系wx：327109739')
    

#input and exit button
btn_input = tkinter.Button(window, text='input', command=usr_input, width=8, height=2)
btn_input.place(x=150, y=680)
btn_help = tkinter.Button(window, text='help', command=usr_help,width=8, height=2)
btn_help.place(x=300, y=680)


window.mainloop()
