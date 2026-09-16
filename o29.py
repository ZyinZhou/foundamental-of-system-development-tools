 import torch
    import torch.nn as nn
    
    # 使用nn.Module定义多项式模型
    class PolyModel(nn.Module):
        def __init__(self):
            super().__init__()
            # 可学习参数 w0,w1,w2,w3
            self.w = nn.Parameter(torch.randn(4) * 0.1)
    
        def forward(self, x):
            # 前向计算：y = w0 + w1*x + w2*x^2 + w3*x^3
            y_pred = self.w[0] + self.w[1]*x + self.w[2]*x**2 + self.w[3]*x**3
            return y_pred
    
    # 准备数据
    torch.manual_seed(0)
    x = torch.linspace(-torch.pi, torch.pi, 200)
    y_true = torch.sin(x)
    
    # 实例化模型、损失函数、优化器
    model = PolyModel()
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
    
    epochs = 10000
    for i in range(epochs):
        # 前向传播
        y_pred = model(x)
        loss = loss_fn(y_pred, y_true)
    
        # 反向传播 + 参数更新
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
        if i % 1000 == 0:
            print(f"epoch {i:5d}, loss={loss.item():.4f}")
    
    # 打印训练后的权重
    print("Learned weights w0,w1,w2,w3 =", model.w.detach().numpy())
