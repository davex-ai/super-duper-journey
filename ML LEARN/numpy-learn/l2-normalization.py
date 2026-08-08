# import numpy as np
#
# # Hyperparameters
# lr = 0.01
# beta = 0.9  # Momentum coefficient
# lambda_reg = 0.01  # L2 regularization strength
# epochs = 1000
#
# # Initialize velocity variables for Momentum (same shape as weights/biases)
# vW1, vW2, vW3 = np.zeros_like(W1), np.zeros_like(W2), np.zeros_like(W3)
# vb1, vb2, vb3 = np.zeros_like(b1), np.zeros_like(b2), np.zeros_like(b3)
#
# for i in range(epochs):
#     # --- Forward Pass ---
#     z1 = np.dot(X, W1) + b1
#     a1 = np.maximum(0, z1)  # ReLU
#     z2 = np.dot(a1, W2) + b2
#     a2 = np.maximum(0, z2)  # ReLU
#     z3 = np.dot(a2, W3) + b3
#     probs = softmax(z3)
#
#     # --- Loss Calculation with L2 ---
#     data_loss = cross_entropy(probs, y)
#     # L2 adds the squared sum of all weights scaled by lambda
#     reg_loss = 0.5 * lambda_reg * (np.sum(W1 ** 2) + np.sum(W2 ** 2) + np.sum(W3 ** 2))
#     total_loss = data_loss + reg_loss
#
#     # --- Backward Pass (Gradients) ---
#     # Standard gradients first (using chain rule)
#     dz3 = probs - y_onehot
#     dW3 = np.dot(a2.T, dz3)
#     db3 = np.sum(dz3, axis=0, keepdims=True)
#
#     # L2 Gradient Update: dL/dW = dLoss_data/dW + lambda * W
#     dW3 += lambda_reg * W3
#
#     # ... (Repeat backprop for W2 and W1, adding lambda_reg * W to each dW)
#
#     # --- Momentum Update Rule ---
#     # 1. Update velocity: v = beta * v - lr * gradient
#     vW3 = beta * vW3 - lr * dW3
#     vb3 = beta * vb3 - lr * db3
#     # 2. Update weights: W = W + v
#     W3 += vW3
#     b3 += vb3
#
#
#     # ... (Repeat for W2, b2, W1, b1)
#
#     # --- Diagnostics ---
#     if i % 50 == 0:
#         # Dead neurons: check where ReLU output is 0 for all samples
#         dead_h1 = np.mean(np.all(a1 <= 0, axis=0)) * 100
#         dead_h2 = np.mean(np.all(a2 <= 0, axis=0)) * 100
#
#         # Gradient Norms: measure the "size" of the updates
#         norm_w1 = np.linalg.norm(dW1)
#         norm_w2 = np.linalg.norm(dW2)
#         norm_w3 = np.linalg.norm(dW3)
#
#         print(f"Epoch {i}\nLoss: {total_loss:.2f}")
#         print(f"Dead H1: {dead_h1:.0f}% | Dead H2: {dead_h2:.0f}%")
#         print(f"||dW1||: {norm_w1:.2f} | ||dW2||: {norm_w2:.2f} | ||dW3||: {norm_w3:.2f}\n")


import numpy as np


# -------- Functions & Derivatives --------
def relu(z): return np.maximum(0, z)


def relu_derivative(z): return (z > 0).astype(float)


def sigmoid(z): return 1 / (1 + np.exp(-z))


# -------- Initialization --------
rng = np.random.default_rng(seed=42)
X = np.array([[2.0, 3.5], [1.0, 2.0], [3.0, 1.0]])
y_true = np.array([1.0, 0.0, 1.0]).reshape(-1, 1)

W1 = rng.standard_normal((4, 2)) * np.sqrt(2 / 2)
b1 = np.zeros((1, 4))
W2 = rng.standard_normal((4, 4)) * np.sqrt(2 / 4)
b2 = np.zeros((1, 4))
W3 = rng.standard_normal((1, 4)) * np.sqrt(2 / 4)
b3 = np.zeros((1, 1))

# 1️⃣ Momentum Variables: Initialize velocity (v) as zeros for all params
vW1, vb1 = np.zeros_like(W1), np.zeros_like(b1)
vW2, vb2 = np.zeros_like(W2), np.zeros_like(b2)
vW3, vb3 = np.zeros_like(W3), np.zeros_like(b3)

lr = 0.01
beta = 0.9  # Momentum coefficient
lambda_reg = 0.01  # 2️⃣ L2 Regularization strength

for epoch in range(200):
    # ---- 1. FORWARD PASS ----
    z1 = X @ W1.T + b1
    a1 = relu(z1)
    z2 = a1 @ W2.T + b2
    a2 = relu(z2)
    z3 = a2 @ W3.T + b3
    a3 = sigmoid(z3)

    # ---- 2. LOSS WITH L2 ----
    # Calculate base Cross-Entropy loss
    data_loss = -np.mean(y_true * np.log(a3 + 1e-9) + (1 - y_true) * np.log(1 - a3 + 1e-9))
    # Add L2 penalty: lambda * sum of squared weights
    reg_loss = lambda_reg * (np.sum(W1 ** 2) + np.sum(W2 ** 2) + np.sum(W3 ** 2))
    loss = data_loss + reg_loss

    # ---- 3. BACKWARD PASS (Chain Rule) ----
    dz3 = a3 - y_true
    # dW3 now includes the gradient of the L2 penalty: lambda * W
    dW3 = (dz3.T @ a2 / len(X)) + (lambda_reg * W3)
    db3 = np.mean(dz3, axis=0)

    da2 = dz3 @ W3
    dz2 = da2 * relu_derivative(z2)
    dW2 = (dz2.T @ a1 / len(X)) + (lambda_reg * W2)
    db2 = np.mean(dz2, axis=0)

    da1 = dz2 @ W2
    dz1 = da1 * relu_derivative(z1)
    dW1 = (dz1.T @ X / len(X)) + (lambda_reg * W1)
    db1 = np.mean(dz1, axis=0)

    # ---- 4. MOMENTUM UPDATE RULE ----
    # v = (beta * old_v) - (lr * gradient)
    vW1 = beta * vW1 - lr * dW1
    vb1 = beta * vb1 - lr * db1
    vW2 = beta * vW2 - lr * dW2
    vb2 = beta * vb2 - lr * db2
    vW3 = beta * vW3 - lr * dW3
    vb3 = beta * vb3 - lr * db3

    # Apply velocity to weights
    W1 += vW1;
    b1 += vb1
    W2 += vW2;
    b2 += vb2
    W3 += vW3;
    b3 += vb3

    # ---- 5. GRADIENT DIAGNOSTICS ----
    if (epoch + 1) % 50 == 0:
        dead_h1 = np.mean(a1 == 0)
        dead_h2 = np.mean(a2 == 0)
        # Calculate Frobenius norms of gradients to monitor signal strength
        norm1, norm2, norm3 = np.linalg.norm(dW1), np.linalg.norm(dW2), np.linalg.norm(dW3)

        print(f"Epoch {epoch + 1}")
        print(f"Loss: {loss:.4f}")
        print(f"Dead H1: {dead_h1:.0%} | Dead H2: {dead_h2:.0%}")
        print(f"||dW1||: {norm1:.4f} | ||dW2||: {norm2:.4f} | ||dW3||: {norm3:.4f}")
        print("-" * 30)
