import pickle
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

with open("latencies_pc_loss_0_combined", 'rb') as p_in:
    latencies1 = pickle.load(p_in)
with open("latencies_pc_loss_10_combined", 'rb') as p_in:
    latencies2 = pickle.load(p_in)
with open("latencies_pc_loss_20_combined", 'rb') as p_in:
    latencies3 = pickle.load(p_in)

x1 = np.linspace(0, len(latencies1), len(latencies1))
x2 = np.linspace(0, len(latencies2), len(latencies2))
x3 = np.linspace(0, len(latencies3), len(latencies3))

n_bins = 200

fig, ax = plt.subplots(1)
latencies = np.array(latencies1)
ax.hist(latencies1, n_bins, density=True, histtype='step',cumulative=True, linewidth=2, label=["No packet loss"])
ax.hist(latencies2, n_bins, density=True, histtype='step',cumulative=True, linewidth=2, label=["10%"])
ax.hist(latencies3, n_bins, density=True, histtype='step',cumulative=True, linewidth=2, label=["20%"])

ax.legend(loc=4)
ax.set_xscale('log')
ax.set_xticks(np.geomspace(1,11,15).round(1))
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

#ax.set_xlim(1,100)
ax.set_title("3 node mediating transfer with varying packet loss PC to PC")
ax.set_xlabel("Transfer latency (seconds)")
ax.set_ylabel("ECDF")
plt.savefig('packet_loss_pc.png')
plt.show()
