# Neuron

import math

# inputs  = [1, 0]
# weights = [0.8, -0.5]
# bias    = -0.2
# y_true  = 1
#
def sigmoid(n):
    return 1 / (1 + math.exp(-n))
#
# def neuron(inputs, weights, bias):
#     total = 0
#     for i in range(len(inputs)):
#         total += inputs[i] * weights[i]
#     total = total + bias
#     return sigmoid(total)
#
# print(neuron(inputs, weights, bias))# 0.6456563062257954

## loss = (y_pred - y_true)**2
# import math

# data
x = 1.0          # input
y_true = 1.0     # correct answer

# parameters (learnable)
w = 0.8
b = -0.2

lr = 0.1         # learning rate

z = w * x + b
y_pred = sigmoid(z)

print("Confidence(sigmoid)", sigmoid(y_pred))

loss = 2 * (y_pred - y_true)
print("Loss", loss)

# How much does prediction change if z changes
dy_dz = y_pred * (1 - y_pred)
print("Loss wrtz", dy_dz)

dz_dw = x
dz_db = 1
print("dz_dw", dz_dw)

dL_dw = loss * dy_dz * dz_dw
dL_db = loss * dy_dz * dz_db

print("dL_dw", dL_dw)
print("dL_db", dL_db)

w = w - lr * dL_dw
b = b - lr * dL_db

print("new w:", w)
print("new b:", b)
