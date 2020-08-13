from tkinter import filedialog
import os
import xlrd
import numpy as np

Folderpath = filedialog.askdirectory()
Filepath = filedialog.askopenfilename()
excel = xlrd.open_workbook(Filepath)
table = excel.sheets()[0]
ncols = table.ncols
r_gene = []
t_gene = []
for i in range(ncols):
    r_gene.append(table.col_values(i)[:3])
    t_gene.append(table.col_values(i)[3:])
i_r = np.array(r_gene,dtype = float)
i_t = np.array(t_gene,dtype = float)
m_i_r = np.mean(i_r, axis=1)
i_dv = []
for i in range(0, ncols):
    i_dv.append(m_i_r[i]-i_t[i])
i_dv = np.array(i_dv)
i_Ct1 = np.power(2, i_dv)
m_i_Ct1 = np.mean(i_Ct1)
std_i_Ct1 = np.std(i_Ct1, ddof=1, axos =1)
cv_i_Ct1 =std_i_Ct1/m_i_Ct1

