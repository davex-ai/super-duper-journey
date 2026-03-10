import random

import numpy as np

heads = 0
trials = 1000

for _ in range(trials):
    if random.random() < 0.5:
        heads += 1

# print(heads / trials)
# print(heads  )
X = np.random.randn(32, 10)
print(X)
# s2e16