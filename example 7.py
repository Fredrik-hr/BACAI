# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:32:41 2024

@author: Mathi
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,101)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x)+np.cos(x)

#                             linestyle                     #v . , 
plt.plot(x,y1,color="r",      ls="-.",      linewidth = 2,  marker=(" ") , label="sinus")
plt.plot(x,y2,color="purple", ls="--",      lw=1,           marker=(" ") , label="cosinus")
plt.plot(x,y3,color="skyblue",ls=(0,(5,1)), lw=1,           marker=(" ") , label="cos+sin")


plt.yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
plt.legend() #makes the box top right
plt.show() #"prints" the graf