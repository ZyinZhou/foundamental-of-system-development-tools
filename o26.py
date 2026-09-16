 import torch

# 生成数据
torch.manual_seed(0)
x = torch.linspace(-torch.pi, torch.pi, 200)
y_true = torch.sin(x)

# 初始化参数w0,w1,w2,w3
w = torch.randn(4) * 0.1

lr = 0.001
epochs = 10000

for i in range(epochs):
    # 前向传播
    y_pred = w[0] + w[1]*x + w[2]*x**2 + w[3]*x**3

    # MSE损失
    loss = torch.mean((y_pred - y_true) ** 2)

    #  手动反向传播：手动求梯度，不使用backward() 
    diff = 2 * (y_pred - y_true)
    grad = torch.zeros_like(w)
    grad[0] = torch.mean(diff)
    grad[1] = torch.mean(diff * x)
    grad[2] = torch.mean(diff * x**2)
    grad[3] = torch.mean(diff * x**3)

    # 参数更新
    w -= lr * grad

    if i % 1000 == 0:
        print(f"epoch {i:5d}, loss={loss.item():.4f}")

print("最终参数 w0,w1,w2,w3 =", w)

