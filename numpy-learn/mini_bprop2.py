import math

# -------- Data --------
x = [2.0, 3.5]
y_true = 1.0

# -------- Parameters --------
w = [0.8, 0.2]
b = -0.2
lr = 5
epochs = 20

def sigmoid(z):
    return 1 / (1 + math.exp(-z))
for epoch in range(epochs):
    # ---- Forward pass ----
    z = sum(xi * wi for xi, wi in zip(x, w)) + b
    y_pred = sigmoid(z)

    # ---- Loss (MSE) ----
    loss = (y_pred - y_true) ** 2

    # ---- Backprop ----
    dL_dy = 2 * (y_pred - y_true) # this is formula for loss wrt pred
    dy_dz = y_pred * (1 - y_pred) # this is formula for pred change wrt z

    dz_dw = x
    dz_db = 1
    #
    dL_dw = [dL_dy * dy_dz * xi for xi in dz_dw]
    dL_db = dL_dy * dy_dz * dz_db

    # ---- Update ----
    w = [wi - lr * dwi for wi, dwi in zip(w, dL_dw)]
    b = b - lr * dL_db

    print(
        f"Epoch {epoch+1:02d} | "
        f"loss={loss:.4f} | "
        f"y_pred={y_pred:.4f} | "
        f"w={w} | b={b:.4f}"
    )