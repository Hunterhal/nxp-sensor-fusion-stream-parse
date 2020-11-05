import numpy as np
import matplotlib.pyplot as plt

with open('data_set.npy', 'rb') as f:
    data_collect = np.load(f)

data_size = data_collect.shape[1]

t = np.arange(data_size)
plt.scatter(t, data_collect[0, :])
plt.scatter(t, data_collect[1, :])
plt.scatter(t, data_collect[2, :])
plt.grid()
plt.show()

print(np.mean(data_collect, axis=1))

plt.hist(data_collect[2, :], bins=np.linspace(-0.3, 0.3, 50, endpoint=True))
plt.grid()
plt.show()
