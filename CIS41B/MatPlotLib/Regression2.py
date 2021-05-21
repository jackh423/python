import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 30
p = 3
x = p * np.random.random((p, 1))
print(type(x))
print(x)
# y = a*x + b with noise
y = 0.01 * x + 1.0 + np.random.normal(size=x.shape)
print(type(x))
print(x)

# create a linear regression model
model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, p, len(x))
y_new = model.predict(x_new[:, np.newaxis])

# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')

plt.show()