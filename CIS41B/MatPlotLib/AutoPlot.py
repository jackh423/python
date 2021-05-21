import matplotlib.pyplot as plt
import random

years = range(2000, 2020)
data = []
for i in range(1,21):
    data.insert(len(data),random.randint(1,100))
plt.plot(years, data)
plt.show()
