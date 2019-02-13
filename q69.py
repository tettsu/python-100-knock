#coding:utf-8

import pandas as pd

df = pd.DataFrame(
    {'名前':
        ['朝倉', '鈴木', '山中', '田中', '山本'],
    '年齢': 
        [17, 43, 40, 12, 62],
    '性別':
    ['男', '男', '女', '男', '女']}
    )

df_1 = df[df['年齢'] < 35]

print(df_1)
