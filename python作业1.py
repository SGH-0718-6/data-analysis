"""
第3题：Carsets (Carseats) 多元线性回归分析
"""
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. 加载数据
from ISLP import load_data
df = load_data('Carseats')

print("=" * 70)
print("数据集基本信息")
print("=" * 70)
print("形状:", df.shape)
print("\n字段列表:", list(df.columns))
print("\nShelveLoc 取值分布:")
print(df['ShelveLoc'].value_counts())
print("\n前5行预览:")
print(df[['Sales', 'Price', 'Income', 'Advertising', 'ShelveLoc']].head())

# 2. 构建回归模型
# 响应变量
y = df['Sales']

# 自变量：连续变量 + 定性变量 ShelveLoc（用虚拟变量处理）
X_cont = df[['Price', 'Income', 'Advertising']].copy()

# 对 ShelveLoc 做哑变量编码，drop_first=True 自动选基准组
X_shelf = pd.get_dummies(df['ShelveLoc'], prefix='ShelveLoc', drop_first=True, dtype=float)

X = pd.concat([X_cont, X_shelf], axis=1)
X = sm.add_constant(X)  # 加入截距项

print("\n" + "=" * 70)
print("自变量矩阵列名（用于判断基准组）")
print("=" * 70)
print(list(X.columns))
print("\n说明：pd.get_dummies(drop_first=True) 会按字母序丢弃第一个类别作为基准组。")
print("ShelveLoc 原始类别: Bad / Good / Medium")
print("按字母序排序: Bad < Good < Medium，因此被丢弃的是 Bad。")

# 3. 拟合 OLS 模型
model = sm.OLS(y, X).fit()

print("\n" + "=" * 70)
print("模型拟合报告 OLS Regression Results")
print("=" * 70)
print(model.summary())

# 4. 计算 VIF
print("\n" + "=" * 70)
print("各变量方差膨胀因子 VIF")
print("=" * 70)
vif_df = pd.DataFrame()
vif_df['variable'] = X.columns
vif_df['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif_df.to_string(index=False))

# 5. 重点系数提取
print("\n" + "=" * 70)
print("关键系数汇总")
print("=" * 70)
coef_df = pd.DataFrame({
    'coef': model.params,
    'std_err': model.bse,
    't': model.tvalues,
    'p_value': model.pvalues
})
print(coef_df.round(4))

print("\nR-squared:", round(model.rsquared, 4))
print("Adj. R-squared:", round(model.rsquared_adj, 4))
