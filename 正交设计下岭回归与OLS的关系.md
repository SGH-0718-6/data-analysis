# 作业1 推导题：证明正交设计下岭回归与OLS估计的关系

## 已知公式
1. OLS估计：

$$
\hat{\mathbf{\beta}}_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
$$

2. 岭回归(Ridge)估计：

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}} = (\mathbf{X}^T\mathbf{X}+\lambda \mathbf{I})^{-1}\mathbf{X}^T\mathbf{Y},\quad \lambda>0
$$

3. 正交设计条件：
$\mathbf{X}^T\mathbf{X}=\mathbf{I}$，
$\mathbf{I}$ 为单位矩阵。

## 证明过程
将正交条件 $\mathbf{X}^T\mathbf{X}=\mathbf{I}$ 代入岭回归闭式解：

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}} = (\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{Y}
$$

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}} = (\mathbf{I}+\lambda \mathbf{I})^{-1}\mathbf{X}^T\mathbf{Y}
$$

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}} = ((1+\lambda)\mathbf{I})^{-1}\mathbf{X}^T\mathbf{Y}
$$

根据单位矩阵求逆性质：

$$
(c\mathbf{I})^{-1}=\frac{1}{c}\mathbf{I}
$$

令 $c=1+\lambda$：

$$
((1+\lambda)\mathbf{I})^{-1}=\frac{1}{1+\lambda}\mathbf{I}
$$


代入得到：

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}} = \frac{1}{1+\lambda}\mathbf{I}\cdot\mathbf{X}^T\mathbf{Y}
$$

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}} =\frac{1}{1+\lambda}\mathbf{X}^T\mathbf{Y}
$$

再看OLS估计，在正交条件 $\mathbf{X}^T\mathbf{X}=\mathbf{I}$ 下：

$$
\hat{\mathbf{\beta}}_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}=\mathbf{I}^{-1}\mathbf{X}^T\mathbf{Y}=\mathbf{X}^T\mathbf{Y}
$$

将 $\hat{\mathbf{\beta}}_{\mathrm{OLS}}=\mathbf{X}^T\mathbf{Y}$ 代入岭回归表达式：

$$
\hat{\mathbf{\beta}}_{\mathrm{Ridge}}=\frac{1}{1+\lambda}\hat{\mathbf{\beta}}_{\mathrm{OLS}}
$$

**证毕**。
