import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import random

# Fixing random state for reproducibility
np.random.seed(random.randint(1,65535))

# histogram our data with numpy
data = np.random.randn(1000)
n, bins = np.histogram(data, 10)

# get the corners of the rectangles for the histogram
left = np.array(bins[:-1])
right = np.array(bins[1:])
bottom = np.zeros(len(left))
top = bottom + n
nrects = len(left)

nbars = nrects * 5
bars = np.zeros((nbars, 2))
codes = np.ones(nbars, int) * path.Path.LINETO
bars[0::5] = path.Path.MOVETO
bars[4::5] = path.Path.CLOSEPOLY
bars[0::5, 0] = left
bars[0::5, 1] = bottom
bars[1::5, 0] = left
bars[1::5, 1] = top
bars[2::5, 0] = right
bars[2::5, 1] = top
bars[3::5, 0] = right
bars[3::5, 1] = bottom

fig, ax = plt.subplots()
barpath = path.Path(bars, codes)
patch = patches.PathPatch(barpath, facecolor='green', edgecolor='blue', alpha=0.5)
ax.add_patch(patch)

ax.set_xlim(left[0], right[-1])
ax.set_ylim(bottom.min(), top.max())
plt.show()