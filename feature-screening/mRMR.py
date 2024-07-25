import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.feature_selection import mutual_info_regression

data = pd.read_excel("D:\pythonproject\医共融合\医工融合代码及文件\data\血液指标统计.xlsx")
y = data['type']
data.drop(columns=['序号'], inplace=True)
data.drop(columns=['type'], inplace=True)

data = (data - data.mean()) / data.std()

X = data


# 计算每个特征与目标变量之间的互信息（mutual information）
mi_scores = mutual_info_regression(X, y)

# 根据互信息选择与目标变量高度相关的特征
selected_features = X.columns[mi_scores > np.mean(mi_scores)]

# 计算所选特征之间的相关性
correlation_matrix = X[selected_features].corr()

# 排除彼此之间高度相关的特征（可以自定义阈值）
highly_correlated_features = set()
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.7:  # 选择相关系数大于 0.7 的特征
            colname = correlation_matrix.columns[i]
            highly_correlated_features.add(colname)

selected_features = selected_features.difference(highly_correlated_features).tolist()

print("选择的特征:", selected_features)
print(len(selected_features))
# sel = data[selected_features]
# sel.to_excel("../data/filtered_data_22.xlsx", index=False)
