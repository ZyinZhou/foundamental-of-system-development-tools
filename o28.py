   import torch

    # 自定义Autograd算子
    class Poly3(torch.autograd.Function):
        @staticmethod
        def forward(ctx, a, b, c, d, x):
            # 前向：y = a + b*(c + d*x)^3
            z = c + d * x
            y = a + b * (z ** 3)
            # 保存需要用于反向传播的变量
            ctx.save_for_backward(a, b, c, d, x, z)
            return y
    
        @staticmethod
        def backward(ctx, grad_output):
            # grad_output: dL/dy
            a, b, c, d, x, z = ctx.saved_tensors
    
            dy_da = torch.ones_like(x)
            dy_db = z**3
            dy_dc = b * 3 * z**2
            dy_dd = b * 3 * z**2 * x
            dy_dx = b * 3 * z**2 * d
    
            dL_da = grad_output * dy_da
            dL_db = grad_output * dy_db
            dL_dc = grad_output * dy_dc
            dL_dd = grad_output * dy_dd
            dL_dx = grad_output * dy_dx
    
            # 返回顺序必须和forward输入一一对应
            return dL_da.sum(), dL_db.sum(), dL_dc.sum(), dL_dd.sum(), dL_dx
    
    # 实例化算子
    poly3_op = Poly3.apply
    
    # 训练：拟合 sin(x)
    torch.manual_seed(0)
    x = torch.linspace(-torch.pi, torch.pi, 200)
    y_true = torch.sin(x)
    
    # 待学习参数 a,b,c,d
    a = torch.tensor(0.1, requires_grad=True)
    b = torch.tensor(0.1, requires_grad=True)
    c = torch.tensor(0.1, requires_grad=True)
    d = torch.tensor(0.1, requires_grad=True)
    
    lr = 1e-4
    epochs = 12000
    
    for i in range(epochs):
        y_pred = poly3_op(a, b, c, d, x)
        loss = torch.mean((y_pred - y_true)**2)
    
        loss.backward()
    
        with torch.no_grad():
            a -= lr * a.grad
            b -= lr * b.grad
            c -= lr * c.grad
            d -= lr * d.grad
    
        # 清空梯度
        a.grad.zero_()
        b.grad.zero_()
        c.grad.zero_()
        d.grad.zero_()
    
        if i % 1000 == 0:
            print(f"epoch {i:5d}, loss = {loss.item():.4f}")
    
    print(f"\nFinal params:\na={a.item():.4f}, b={b.item():.4f}, c={c.item():.4f}, d={d.item():.4f}")
