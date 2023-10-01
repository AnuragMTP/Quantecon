# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:49:12 2023

@author: anura
RE investment idea analysis
"""
#rates
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
max= -1000
min= 1000

i_r=np.arange(0.07,.2025,0.0025) #interest rate 7-20%
l_r=np.arange(.10,.75,0.025)#lending rate 10-75%
c=1.0#capital/cost taken as 1
r_r=np.arange(0.01,0.08,0.00125)#rent rate 1-8% conservative?

res=np.empty((len(r_r),len(i_r),len(l_r)))

#coc rate
for i in range(len(r_r)):
    for j in range(len(i_r)):
        for k in range(len(l_r)):
            m_c=i_r[j]*c*l_r[k]#mortage cost
            inc=c*r_r[i]#income
            cost=c*(1.05-l_r[k]) #cost, including allied at 5%
            res[i][j][k]=100*(inc-m_c)/cost
            if (100*(inc-m_c)/cost)>max:
                max=100*(inc-m_c)/cost
                maxdict=dict(i_r=i_r[j],r_r=r_r[i],l_r=l_r[k], coc=max)
            elif (100*(inc-m_c)/cost)<min:
                min=100*(inc-m_c)/cost
                mindict=dict(i_r=i_r[j],r_r=r_r[i],l_r=l_r[k], coc=min)
            else:
                #nop
                continue
