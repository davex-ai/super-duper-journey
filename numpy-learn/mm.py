import numpy as np


# -------- Functions --------
def relu(z):
    return np.maximum(0, z)


def relu_derivative(z):
    # 1 if z > 0, otherwise 0
    return (z > 0).astype(float)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# -------- Initialization --------
X = np.array([[2.0, 3.5], [1.0, 2.0], [3.0, 1.0]])  # (3,2)
y_true = np.array([1.0, 0.0, 1.0]).reshape(-1, 1)  # (3,1) - keep column shape

W1 = np.random.randn(2, 2) * 0.01
b1 = np.zeros((1, 2))
W2 = np.random.randn(1, 2) * 0.01
b2 = np.zeros((1, 1))

lr = 0.1

for epoch in range(100):
    # ---- 1. FORWARD PASS ----
    z1 = X @ W1.T + b1  # (3,2)
    a1 = relu(z1)  # (3,2) - Hidden activation

    z2 = a1 @ W2.T + b2  # (3,1)
    a2 = sigmoid(z2)  # (3,1) - Output probability

    # ---- 2. TRACK LOSS & ACCURACY ----
    # BCE Loss: -[y*log(a2) + (1-y)*log(1-a2)]
    loss = -np.mean(y_true * np.log(a2 + 1e-9) + (1 - y_true) * np.log(1 - a2 + 1e-9))

    predictions = (a2 > 0.5).astype(float) #i dont get wats happening here
    accuracy = np.mean(predictions == y_true) #i dont get wats happening here

    # ---- 3. BACKWARD PASS (The "Blame" Game) ----  u lost me here

    # Error at Output: For BCE + Sigmoid, the gradient is simply (Pred - True)
    # This is a beautiful mathematical shortcut!
    dz2 = a2 - y_true  # (3,1)

    # dW2 = error * input
    dW2 = dz2.T @ a1 / X.shape[0] # would len(x) work here?
    db2 = np.mean(dz2, axis=0)

    # Backprop to Hidden Layer
    da1 = dz2 @ W2  # How much hidden layer values affect error
    dz1 = da1 * relu_derivative(z1)  # Zero out "blame" where ReLU was off

    # dW1 = error * input
    dW1 = dz1.T @ X / X.shape[0]
    db1 = np.mean(dz1, axis=0)

    # ---- 4. UPDATE ----
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch + 1} | Loss: {loss:.4f} | Acc: {accuracy:.2f}")
