import pickle
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

with open("latencies_rpi", 'rb') as p_in:
    latencies = pickle.load(p_in)

x = np.linspace(0, len(latencies), len(latencies))


fig, ax = plt.subplots(2)
latencies = np.array(latencies)

ax[0].stem(x, latencies[:,0])
ax[0].set_title("From PC to Pi Zero")
ax[1].stem(x, latencies[:,1])
ax[1].set_title("From Pi Zero to PC")
ax[1].set_ylabel("Transfer latency (seconds)")
plt.savefig("latency_direct.png")
plt.show()