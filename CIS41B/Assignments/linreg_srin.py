import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = [[1850, 1851, 1852, 1853, 1854, 1855]]
y = [[-0.373, -0.218, -0.228, -0.269, -0.248, -0.272]]
X = np.array(x).reshape(-1, 1)
Y = np.array(y).reshape(-1, 1)
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(x)  # make predictions
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()