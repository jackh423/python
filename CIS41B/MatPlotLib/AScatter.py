import numpy as np
import scipy as sp
import matplotlib.pylab as plt

n = 512
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X,Y)
plt.show()
