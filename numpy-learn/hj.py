# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]
#
# w = 0
# lr = 0.1
#
# for step in range(20):
#     total_gradient = 0
#
#     for i in range(len(x)):
#         y_pred = w * x[i]
#         error = y_pred - y[i]
#         gradient = 2 * error * x[i]
#         total_gradient += gradient
#
#     avg_gradient = total_gradient / len(x)
#     w = w - lr * avg_gradient
#
#     print("step:", step, "w:", w)

X = [
    [2, 5],
    [1, 3],
    [3, 6],
    [4, 8]
]

y = [65, 50, 80, 95]

w = [0, 0]
lr = 0.01

for step in range(100):
    grad = [0, 0]

    for i in range(len(X)):
        y_pred = w[0] * X[i][0] + w[1] * X[i][1]
        error = y_pred - y[i]

        grad[0] += 2 * error * X[i][0]
        grad[1] += 2 * error * X[i][1]

    grad[0] /= len(X)
    grad[1] /= len(X)

    w[0] -= lr * grad[0]
    w[1] -= lr * grad[1]

    if step % 10 == 0:
        print(step, w)