import numpy as np

# -------- Data --------
x = np.array([2.0, 3.5])
y_true = 1.0

# -------- Parameters --------
w = np.array([0.8, 0.2])
b = -0.2
lr = 0.1
epochs = 20

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for epoch in range(epochs):
    # ---- Forward ----
    z = np.dot(w, x) + b
    y_pred = sigmoid(z)

    X = np.array([
        [2.0, 3.5],
        [1.0, 2.0],
        [3.0, 1.0]
    ])
    w = np.array([0.8, 0.2])
    for i in range(len(X)):
        zi = np.dot(w, X[i]) + b

    # ---- Loss ----
    loss = (y_pred - y_true) ** 2

    # ---- Backprop ----
    dL_dy = 2 * (y_pred - y_true)
    dy_dz = y_pred * (1 - y_pred)

    dL_dz = dL_dy * dy_dz
    dL_dw = dL_dz * x
    dL_db = dL_dz

    # ---- Update ----
    w -= lr * dL_dw
    b -= lr * dL_db

    print(
        f"Epoch {epoch+1:02d} | "
        f"loss={loss:.4f} | "
        f"y_pred={y_pred:.4f} | "
        f"w={w} | b={b:.4f}"
    )