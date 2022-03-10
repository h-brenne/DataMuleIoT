import pickle
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

with open("latencies_rpi_mediating", 'rb') as p_in:
    latencies = pickle.load(p_in)

x = np.linspace(0, len(latencies), len(latencies))


fig, ax = plt.subplots()
latencies = np.array(latencies)

ax.stem(x, latencies[:,0])
plt.show()