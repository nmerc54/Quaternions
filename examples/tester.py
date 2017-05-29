'''
=========================================
Labeling ticks using engineering notation
=========================================

Demo to show use of the engineering Formatter.
'''

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import EngFormatter

prng = np.random.RandomState(123)

fig, ax = plt.subplots()
ax.set_xscale('log')
formatter = EngFormatter(unit='Hz')
ax.xaxis.set_major_formatter(formatter)

xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
ax.plot(xs, ys)

plt.show()


"""
# -*- noplot -*-

=============================
The object-oriented interface
=============================

A pure OO (look Ma, no pylab!) example using the agg backend

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3])
ax.set_title('hi mom')
ax.grid(True)
ax.set_xlabel('time')
ax.set_ylabel('volts')
canvas.print_figure('test')
"""
