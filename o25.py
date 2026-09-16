import numpy as np
import matplotlib.pyplot as plt

# 生成训练数据
np.random.seed(0)
x = np.linspace(-np.pi, np.pi, 200)
y_true = np.sin(x)

# 初始化多项式参数 w0,w1,w2,w3
w = np.random.randn(4) * 0.1

lr = 0.001
epochs = 10000

for i in range(epochs):
    # 前向传播
    y_pred = w[0] + w[1]*x + w[2]*x**2 + w[3]*x**3

    # MSE损失
    loss = np.mean((y_pred - y_true)**2)

    # 手动反向传播，求梯度
    grad = np.zeros_like(w)
    grad[0] = np.mean(2 * (y_pred - y_true))
    grad[1] = np.mean(2 * (y_pred - y_true) * x)
    grad[2] = np.mean(2 * (y_pred - y_true) * x**2)
    grad[3] = np.mean(2 * (y_pred - y_true) * x**3)

    # 参数更新
    w -= lr * grad

    if i % 1000 == 0:
        print(f"epoch {i:5d}, loss={loss:.4f}")

# 绘图
plt.plot(x, y_true, label="sin(x)")
plt.plot(x, y_pred, label="3rd poly fit", linestyle="--")
plt.legend()
plt.show()
print("最终参数 w0,w1,w2,w3 =", w)
