import numpy as np


# -------- Functions & Derivatives --------
def relu(z): return np.maximum(0, z)


def relu_derivative(z): return (z > 0).astype(float)


def sigmoid(z): return 1 / (1 + np.exp(-z))


# -------- Initialization (He Initialization for ReLU) --------
np.random.default_rng(seed=42)
X = np.array([[2.0, 3.5], [1.0, 2.0], [3.0, 1.0]])  # (3,2)
y_true = np.array([1.0, 0.0, 1.0]).reshape(-1, 1)

# Multiple Hidden Layers: Input(2) -> H1(4) -> H2(4) -> Out(1)
# Using He initialization (sqrt(2/fan_in)) helps prevent early "death"
W1 = np.random.randn(4, 2) * np.sqrt(2 / 2) #
print("w1",W1)
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 4) * np.sqrt(2 / 4)
b2 = np.zeros((1, 4))
W3 = np.random.randn(1, 4) * np.sqrt(2 / 4)
b3 = np.zeros((1, 1))

lr = 0.01  # Sensitivity: Lower LR helps prevent Dying ReLU

for epoch in range(200):
    # ---- 1. FORWARD PASS (ReLU Everywhere) ----
    z1 = X @ W1.T + b1
    a1 = relu(z1)

    z2 = a1 @ W2.T + b2
    a2 = relu(z2)

    z3 = a2 @ W3.T + b3
    a3 = sigmoid(z3)  # Final layer stays Sigmoid for binary probability

    # ---- 2. TRACK LOSS & ACCURACY ----
    loss = -np.mean(y_true * np.log(a3 + 1e-9) + (1 - y_true) * np.log(1 - a3 + 1e-9))

    # ---- 3. DYING RELU DIAGNOSIS (Numerical) ----
    # Detection: Fraction of neurons in a layer that are outputting 0
    dead_h1 = np.mean(a1 == 0)
    dead_h2 = np.mean(a2 == 0)

    # ---- 4. BACKWARD PASS (Chain Rule through Layers) ----
    dz3 = a3 - y_true

    dW3 = dz3.T @ a2 / len(X)
    db3 = np.mean(dz3, axis=0)

    # Backprop to H2
    da2 = dz3 @ W3
    dz2 = da2 * relu_derivative(z2)  # Mutes gradient where ReLU is dead
    dW2 = dz2.T @ a1 / len(X)
    db2 = np.mean(dz2, axis=0)

    # Backprop to H1
    da1 = dz2 @ W2
    dz1 = da1 * relu_derivative(z1)
    dW1 = dz1.T @ X / len(X)
    db1 = np.mean(dz1, axis=0)

    # ---- 5. UPDATE ----
    W3 -= lr * dW3;
    b3 -= lr * db3
    W2 -= lr * dW2;
    b2 -= lr * db2
    W1 -= lr * dW1;
    b1 -= lr * db1

    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch + 1} | Loss: {loss:.4f} | Dead H1: {dead_h1:.1%} | Dead H2: {dead_h2:.1%}")
