import numpy as np
import pandas as pd
import random

rows = []
for _ in range(2000):
    n = random.randint(3, 15)
    bursts = np.random.randint(1, 20, n)
    arrivals = np.sort(np.random.randint(0, 10, n))
    features = [
        n,
        np.mean(bursts),
        np.std(bursts),
        np.mean(arrivals),
        np.std(arrivals),
        np.min(bursts),
        np.max(bursts),
        np.min(arrivals),
        np.max(arrivals)
    ]
    # Simulate which algo is best: SJF for high burst std, RR for high arrival std, FCFS otherwise
    if np.std(bursts) > 5:
        label = 1  # SJF
    elif np.std(arrivals) > 3:
        label = 2  # RR
    else:
        label = 0  # FCFS
    row = features + [label]
    rows.append(row)

columns = [
    'num_tasks','burst_mean','burst_std','arrival_mean','arrival_std',
    'burst_min','burst_max','arrival_min','arrival_max','best_algo'
]
df = pd.DataFrame(rows, columns=columns)
df.to_csv('scheduling_dataset.csv', index=False)
print('Dataset saved as scheduling_dataset.csv')