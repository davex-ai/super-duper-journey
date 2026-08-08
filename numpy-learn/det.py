import numpy as np

# -------- Tiny Dataset --------
X = np.array([
    [2.0, 3.5],   # sample 1
    [1.0, 2.0],   # sample 2
    [3.0, 1.0]    # sample 3
])                  # shape (3,2) → 3 samples, 2 features

y_true = np.array([1.0, 0.0, 1.0])  # targets for each sample

# -------- Initialize Parameters --------
# Hidden layer (2 neurons)
W1 = np.random.randn(2, 2)  # why does this have 2,2 and w2 have 2,1
print('w1', W1)
b1 = np.zeros(2)             # one bias per neuron
print('b1', b1)

# Output layer (1 neuron)
W2 = np.random.randn(1, 2)  # shape (output_neurons, hidden_neurons)
print('W1', W1)
b2 = np.zeros(1)
print('b2', b2)

lr = 0.1  # learning rate
epochs = 5  # small for demonstration

# -------- Activation Function --------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(a):
    return a * (1 - a)  # derivative in terms of activated output

for epoch in range(epochs):
    # ---- FORWARD PASS ----
    # Hidden layer
    z1 = X @ W1.T + b1          # shape (3,2) → one z per neuron per sample
    print('z1', z1)
    a1 = sigmoid(z1)             # activated output of hidden layer
    print('a1', a1)

    # Output layer
    z2 = a1 @ W2.T + b2          # shape (3,1)
    print('z1', z2)
    a2 = sigmoid(z2)             # final prediction
    print('a2', a2)

    # ---- LOSS (Mean Squared Error) ----
    loss = np.mean((a2.flatten() - y_true) ** 2)
    print('a2', a2)

    # ---- BACKWARD PASS ----
    # Output layer
    dL_da2 = 2 * (a2.flatten() - y_true)        # blame at output
    da2_dz2 = sigmoid_derivative(a2).flatten()  # how output changes wrt z2
    dL_dz2 = dL_da2 * da2_dz2                   # chain rule

    # Gradients for W2 and b2
    dL_dW2 = dL_dz2[:, None] @ a1               # outer product: (samples,1) @ (samples,hidden)
    dL_dW2 = np.mean(dL_dW2, axis=0, keepdims=True)  # average over samples
    dL_db2 = np.mean(dL_dz2)                     # bias gradient

    # Hidden layer (propagate blame)
    dL_da1 = dL_dz2[:, None] @ W2               # shape: (samples, hidden_neurons)
    dL_dz1 = dL_da1 * sigmoid_derivative(a1)    # chain rule through hidden layer

    # Gradients for W1 and b1
    dL_dW1 = dL_dz1.T @ X                       # shape (hidden, input_features)
    dL_dW1 /= X.shape[0]                        # average over samples
    dL_db1 = np.mean(dL_dz1, axis=0)            # average over samples

    # ---- UPDATE PARAMETERS ----
    W2 -= lr * dL_dW2
    b2 -= lr * dL_db2
    W1 -= lr * dL_dW1
    b1 -= lr * dL_db1

    # ---- Print for debugging ----
    print(f"Epoch {epoch+1} | Loss: {loss:.4f} | Predictions: {a2.flatten()}")