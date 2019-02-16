#coding:utf-8

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {'名前':
        ['朝倉', '鈴木', '山中', '田中', '山本'],
    '年齢': 
        [17, 43, 40, 12, 62],
    '性別':
    ['男', '男', '女', '男', '女']}
    )

row = pd.DataFrame(
    {
        '名前': ['池田'],
        '年齢': [1989],
        '性別': ['男']
        }
    )
df_2 = pd.concat([df,row], axis=0)
df_2

df_2.index = np.arange(len(df_2))
df_2

df_2['居住地'] = ['東京','大阪','北海道','宮城','富山','大分']
df_2

print(df_2)