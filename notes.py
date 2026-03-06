# Goal: Predict a continuous value. No activation function. Loss is MSE.


import numpy as np

# Data: 3 samples, 2 features (e.g., Square footage, Age of house)
X = np.array([[2.0, 3.5], [1.0, 2.0], [3.0, 1.0]])
y_true = np.array([[500.0], [300.0], [450.0]])  # Continuous prices

# Init: (2 features -> 1 output)
W = np.random.randn(2, 1) * 0.01
b = np.zeros((1, 1))
lr = 0.01

for i in range(100):
    # Forward
    y_pred = X @ W + b

    # Loss (MSE)
    loss = np.mean((y_pred - y_true) ** 2)

    # Backprop: Derivative of (pred-true)^2 is 2*(pred-true)
    dz = 2 * (y_pred - y_true) / len(X)
    dW = X.T @ dz
    db = np.sum(dz, axis=0, keepdims=True)

    # Update
    W -= lr * dW
    b -= lr * db

# 2.  Logistic Regression(Simple)
# Goal: Binary classification with 1 layer.Activation is Sigmoid.Loss is BCE.

# Data: Same X, but y is 0 or 1
y_true = np.array([[1.0], [0.0], [1.0]])

W = np.random.randn(2, 1) * 0.01
b = np.zeros((1, 1))

for i in range(100):
    # Forward
    z = X @ W + b
    a = 1 / (1 + np.exp(-z))  # Sigmoid

    # Loss (BCE)
    loss = -np.mean(y_true * np.log(a + 1e-9) + (1 - y_true) * np.log(1 - a + 1e-9))

    # Backprop (The BCE + Sigmoid Shortcut)
    dz = a - y_true
    dW = X.T @ dz / len(X)
    db = np.mean(dz, axis=0, keepdims=True)

    W -= lr * dW
    b -= lr * db

# 3. Logistic Regression(Deep Neural Network)
# Goal: Binary classification with Hidden Layers.ReLU for hidden, Sigmoid for output.

# Architecture: Input(2) -> H1(4) -> H2(4) -> Out(1)
# He Initialization: sqrt(2/fan_in)
W1 = np.random.randn(2, 4) * np.sqrt(2 / 2);
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 4) * np.sqrt(2 / 4);
b2 = np.zeros((1, 4))
W3 = np.random.randn(4, 1) * np.sqrt(2 / 4);
b3 = np.zeros((1, 1))

for i in range(200):
    # --- Forward ---
    z1 = X @ W1 + b1;
    a1 = np.maximum(0, z1)  # ReLU
    z2 = a1 @ W2 + b2;
    a2 = np.maximum(0, z2)  # ReLU
    z3 = a2 @ W3 + b3;
    a3 = 1 / (1 + np.exp(-z3))  # Sigmoid Output

    # --- Backprop (The Chain) ---
    dz3 = a3 - y_true  # Output Error
    dW3 = a2.T @ dz3 / len(X)
    db3 = np.mean(dz3, axis=0, keepdims=True)

    da2 = dz3 @ W3.T  # Pass back to H2
    dz2 = da2 * (z2 > 0)  # ReLU deriv
    dW2 = a1.T @ dz2 / len(X)
    db2 = np.mean(dz2, axis=0, keepdims=True)

    da1 = dz2 @ W2.T  # Pass back to H1
    dz1 = da1 * (z1 > 0)  # ReLU deriv
    dW1 = X.T @ dz1 / len(X)
    db1 = np.mean(dz1, axis=0, keepdims=True)

    # --- Update ---
    W3 -= lr * dW3;
    b3 -= lr * db3
    W2 -= lr * dW2;
    b2 -= lr * db2
    W1 -= lr * dW1;
    b1 -= lr * db1


