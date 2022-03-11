import pickle

def combine_data(latencies):
    latencies_combined = []
    for pair in latencies:
        latencies_combined.append(pair[0])
        latencies_combined.append(pair[1])
    return latencies_combined

file = "latencies_pc_loss_20"
with open(file, 'rb') as p_in:
    latencies = pickle.load(p_in)

latencies_combined = combine_data(latencies)

with open(file + "_combined", 'wb') as out:
    pickle.dump(latencies_combined, out, pickle.HIGHEST_PROTOCOL)