# Weekly Task 08; plottask.py
# This program isplays a plot of the following functions:
# f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.
# References: https://queirozf.com/entries/matplotlib-pyplot-by-example
# Author: Ross Downey

import numpy as np 
import matplotlib.pyplot as plt # importing correct modules

xpoints = np.array([0, 1, 2, 3, 4])
gpoints = xpoints**2
hpoints = xpoints**3 # setting array values for each plot, squaring and cubing original array

plt.plot (xpoints, marker = 'o', mec = 'tab:orange', mfc = 'tab:orange',
ms = 7)
plt.plot (gpoints, marker = 'o', mec = 'c', mfc = 'c',
ms = 7, ls = 'dashed')
plt.plot (hpoints, marker = 'o', mec = 'r', mfc = 'r',
ms = 7, ls = 'dashed') # formatting plot colours, appearance, point size, dashed lines etc.
plt.title("Weekly Task 08: Plottask.py")
plt.xlabel('x', color='k', fontsize=15)
plt.ylabel('f(x) / g(x) / h(x)', color='k', fontsize=15) # formatting title and axis labels
plt.legend(['f(x)=x', 'g(x)=x^2', 'h(x)=x^3'], loc = 'upper center') # format legend labels and location
plt.grid() # Think the grid makes it appear nicer
plt.savefig('threeFunctions.png') # Saving plot