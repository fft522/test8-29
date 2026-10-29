import pandas as pd
# 读取数据
df1 = pd.read_csv('train_8_remaining_recalc.csv',encoding='utf-8')
# 将绝对值小于15的行保留

df1 = df1[abs(df1['ETAerror'])<15]
print(df1.shape)
print(df1['ETAerror'].max())
print(df1['ETAerror'].min())
df1.to_csv('train_8_remaining_recalc_15.csv',index=False)
