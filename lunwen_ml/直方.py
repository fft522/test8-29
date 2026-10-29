import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']          # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False            # 解决负号 '-' 显示为方块的问题
# 读取数据
df = pd.read_excel(r'C:\Users\86130\Desktop\船舶数据处理\filtered_merged_big_data.xlsx')
print(df.columns)

# 提取 time_gap 列，忽略 NaN（若有）
data = df['time_gap'].dropna()

# 设置区间边界：从 -10 到 20，步长 1
bins = np.arange(-10, 20.1, 2)   # 20.1 确保包含 20

# 绘制频数直方图
plt.figure(figsize=(10, 6))
counts, bins_edges, patches = plt.hist(data, bins=bins, edgecolor='black', alpha=0.7)

# 添加标题和标签
# plt.title('频数直方图 - time_gap')
plt.xlabel('time_gap')
plt.ylabel('频数')

# 可选：显示每个柱子的频数（在柱子顶部显示数字）
# for count, edge in zip(counts, bins_edges[:-1]):
#     if count > 0:
#         plt.text(edge + 0.5, count, int(count), ha='center', va='bottom', fontsize=8)

# 显示网格（可选）
plt.grid(axis='y', linestyle='--', alpha=0.3)

# 显示图形
plt.show()