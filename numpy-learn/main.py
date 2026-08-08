# Neuron

import math

inputs  = [1, 0]
weights = [0.8, -0.5]
bias    = -0.2
y_true  = 1

def sigmoid(n):
    return 1 / (1 + math.exp(-n))

def neuron(inputs, weights, bias):
    total = 0
    for i in range(len(inputs)):
        total += inputs[i] * weights[i]
    total = total + bias
    return sigmoid(total)
#
print(neuron(inputs, weights, bias))# 0.6456563062257954

## loss = (y_pred - y_true)**2

