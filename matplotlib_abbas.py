# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:32:04 2024

@author: Mathi
"""

#                        as is just a rename
import matplotlib.pyplot as plt

#fig = plt.figure(figsize=(8, 6), dpi=80)

#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

#axes = fig.add_axes([0, 0, 1, 1])
#axes = fig.add_axes([0.1, 0.1, 0.3, 0.3])
#axes = fig.add_axes([0.4, 0.6, 0.3, 0.3])
#axes = fig.add_axes([0.5, 0.1, 0.3, 0.3])

#fig , ax = plt.subplots (nrows = 2, ncols = 2, figsize=(8, 6))


#fig , ax = plt.subplots (nrows = 2, ncols = 2, sharex=True, sharey=True, figsize=(8,6))

x = [0, 1, 2, 3, 4, 5, ]
y = [1, 2.718, 7.389, 20.085, 54.598, 148.413]
y2 = [ 0, 2, 8, 18, 32, 50]

#fig , ax = plt.subplots (figsize=(8, 6))
#ax.plot(x,y)

#you can do this instead of the right above (its the same thing)
plt.plot(x,y)
plt.plot(x, y2)

#titel and labels
fig = plt.gcf()
ax = plt.gca()

ax.set_title("Sample Plot")
ax.set_xlabel("X Axis Label")
ax.set_ylabel("Y Axis Label")
ax.set(xlim = (0, 5))
ax.set(ylim = (0, 150))
plt.xticks([0,1, 2, 3, 4, 5, 10])
plt.yticks([0, 25, 50, 75, 100, 125, 150])
plt.grid(True)
#plt.savefig("fig_name.png")

plt.show()

