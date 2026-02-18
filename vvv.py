import random

heads = 0
trials = 1000

for _ in range(trials):
    if random.random() < 0.5:
        heads += 1

print(heads / trials)
print(heads  )