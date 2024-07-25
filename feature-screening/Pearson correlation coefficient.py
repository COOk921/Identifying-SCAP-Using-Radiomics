import pandas as pd

import numpy as np
from sklearn.preprocessing import StandardScaler

data = pd.read_excel("D:\pythonproject\医共融合\医工融合代码及文件\data\血液指标统计.xlsx")
data.drop(columns=['序号'], inplace=True)
data = (data - data.mean()) / data.std()

# 计算每个特征与目标变量之间的皮尔逊相关系数
correlation_matrix = data.corr()
correlation_with_target = correlation_matrix['type'].abs().sort_values(ascending=False)

# 选择相关系数大于阈值的特征
threshold = 0.5  # 选择相关系数大于 0.5 的特征
print(correlation_with_target)
selected_features = correlation_with_target[correlation_with_target > threshold].index.tolist()


print("选择的特征:", selected_features)
