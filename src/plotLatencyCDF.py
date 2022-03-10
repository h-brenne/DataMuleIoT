import pickle
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

with open("latencies_rpi_5_mediating", 'rb') as p_in:
    latencies = pickle.load(p_in)

x = np.linspace(0, len(latencies), len(latencies))
n_bins = 200

fig, ax = plt.subplots()
latencies = np.array(latencies)
ax.hist(latencies, n_bins, density=True, histtype='step',cumulative=True, linewidth=2, label=["From PC to Pi Zero","From Pi Zero to PC"])
ax.legend()
ax.set_xscale('log')
ax.set_xticks(np.geomspace(1,70,15).round(1))
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax.set_xlabel("Transfer latency (seconds)")
ax.set_ylabel("ECDF")
plt.show()