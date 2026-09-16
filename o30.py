 import torch
    import torch.nn as nn
    
    # 使用 nn.Module 定义三次多项式模型
    class PolyModel(nn.Module):
        def __init__(self):
            super().__init__()
            # 4个可学习参数 w0,w1,w2,w3
            self.w = nn.Parameter(torch.randn(4) * 0.1)
    
        def forward(self, x):
            # y = w0 + w1*x + w2*x^2 + w3*x^3
            y_pred = self.w[0] + self.w[1]*x + self.w[2]*x**2 + self.w[3]*x**3
            return y_pred
    
    # 构造训练数据 sin(x)
    torch.manual_seed(0)
    x = torch.linspace(-torch.pi, torch.pi, 200)
    y_true = torch.sin(x)
    
    model = PolyModel()
    loss_fn = nn.MSELoss()
    
    # ========== optim包：RMSprop优化器 ==========
    optimizer = torch.optim.RMSprop(model.parameters(), lr=0.001)
    
    epochs = 10000
    for i in range(epochs):
        y_pred = model(x)
        loss = loss_fn(y_pred, y_true)
    
        optimizer.zero_grad()   # 清空上一轮梯度
        loss.backward()         # 自动反向传播求梯度
        optimizer.step()        # RMSprop 更新参数
    
        if i % 1000 == 0:
            print(f"epoch {i:5d}, loss={loss.item():.4f}")
    
    print("Learned weights w0,w1,w2,w3 =", model.w.detach().numpy())
