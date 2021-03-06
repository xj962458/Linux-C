## 实例：学习XOR函数
**XOR 函数(‘‘异或’’ 逻辑)是两个二进制值 x1 和 x2 的运算。当这些二进制值 中恰好有一个为 1 时，XOR 函数返回值为 1。其余情况下返回值为 0。XOR 函数提 供了我们想要学习的目标函数 y = $f^{*}(x)$。我们的模型给出了一个函数 y = f(x;θ) 并且我们的学习算法会不断调整参数 θ 来使得 f 尽可能接近**
**$f^{*}$**  
**我们现在必须要选择我们模型 f(x;θ) 的形式。假设我们选择一个线性模型，θ ,包含 w 和 b，那么我们的模型被定义成$f(x;w,b) = x^{T}w+b$,我们可以使用正规方程关于 w 和 b 最小化 J(θ)，来得到一个闭式解。解正规方程以后，我们得到 w = 0 以及 b = 1 。线性模型仅仅是在任意一点都输出0.5。**  
### 线性模型为什么不能用来表示 XOR 函 数。解决这个问题的其中一种方法是使用一个模型来学习一个不同的特征空间，在 这个空间上线性模型能够表示这个解。
**具体来说，我们这里引入一个非常简单的前馈神经网络，它有一层隐藏层并且隐 藏层中包含两个单元。这个前馈网络有一个通过函数 $f^{(1)}(x;W,c)$ 计算得到的隐藏单元的向量 h。这些隐藏单元的值随后被用作第二层的 输入。第二层就是这个网络的输出层。输出层仍然只是一个线性回归模型，只不过现在它作用于 h 而不是 x。网络现在包含链接在一起的两个函数:h = $f^{(1)}$ (x; W, c) 和 y = $f^{(2)}$(h; w, b)，完整的模型是 f(x; W, c, w, b) = 
$f^{(2)}(f^{(1)}(x))$。**  
**显然，我们必须用非线性函数来描述这些特征。大多数神经网络通过仿射变换之 后紧跟着一个被称为激活函数的固定非线性函数来实现这个目标，其中仿射变换由 学得的参数控制。我们这里使用这种策略，定义 h = $g(W^{⊤}x + c)$，其中 W 是线性 变换的权重矩阵，c 是偏置。此前，为了描述线性回归模型，我们使用权重向量和一 个标量的偏置参数来描述从输入向量到输出标量的仿射变换。现在，因为我们描述 的是向量 x 到向量 h 的仿射变换，所以我们需要一整个向量的偏置参数。激活函数 g 通常选择对每个元素分别起作用的函数，有 hi = $g(x^{⊤}W:,i + ci)$。在现代神经网络中，默认的推荐是使用由激活函数 g(z) = max{0, z} 定义的 整流线性单元(rectified linear unit)或者称为 ReLU**
