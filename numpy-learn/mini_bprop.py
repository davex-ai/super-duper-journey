import math

# data
x = 1.0
y_true = 1.0

# parameters
w = 0.8
b = -0.2
lr = 0.1

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# ---- Forward pass ----
z = w * x + b
y_pred =  z

print("z:", z)
print("y_pred:", y_pred)

# ---- Loss ----
loss = (y_pred - y_true) ** 2
print("loss:", loss)

# ---- Backprop ----

# A. dL/dy_pred
dL_dy = 2 * (y_pred - y_true)
print("dL/dy:", dL_dy)

# B. dy_pred/dz
dy_dz = y_pred * (1 - y_pred)
print("dy/dz:", dy_dz)

# C. dz/dw, dz/db
dz_dw = x
dz_db = 1

# ---- Chain rule ----
dL_dw = dL_dy * dy_dz * dz_dw
dL_db = dL_dy * dy_dz * dz_db

print("dL/dw:", dL_dw)
print("dL/db:", dL_db)

# ---- Update ----
w = w - lr * dL_dw
b = b - lr * dL_db

print("new w:", w)
print("new b:", b)
