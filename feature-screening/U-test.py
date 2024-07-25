from scipy.stats import mannwhitneyu
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = pd.read_excel("D:\pythonproject\医共融合\医工融合代码及文件\data\血液指标统计.xlsx")#.sample(frac=1, random_state=42)




group2 = data['type'].values
cnt =0
for column in data.columns:
    if(column  == '序号' or column=='type'):
        continue
    group1 =data[column].values
    mean_val = np.mean(group1)
    std_dev = np.std(group1)

    # 进行 Z-Score 归一化
    group1 = (group1 - mean_val) / std_dev

    statistic, p_value = mannwhitneyu(group1, group2)
    if p_value > 0.05:
        print(column)
        #print("Mann-Whitney U 检验统计量:", statistic)
        print("p值:", p_value)
        cnt+=1
print(cnt)