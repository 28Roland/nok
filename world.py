import pandas as pd
import os
import json
import jieba
import xlsxwriter
from openpyxl import *
jieba.load_userdict('./userdict.txt')
df=pd.read_json(r'./credix03.json')


wb_list=[]
wc_list=[]
k=len(df.loc['標題'])
print(k)
for i in range(k):
    ja=df[i]['內文']
    gg=jieba.lcut(ja)
    # print(gg)
    wb_list.append(gg)
    word_c={}
    for i in gg:
        if i in word_c:
            word_c[i] +=1
        else:
            word_c[i] =1
    wc_list.append(word_c)

df.loc['斷詞']=wb_list
df.loc['詞頻']=wc_list
print(df)

df.to_json('credix03.json',orient='index',force_ascii=False)
df.to_csv('credcsv03.csv',encoding='utf-8')
# df.to_excel('credexcel03.xlsx')





# with open("./credix03.json") as g:
# 	result_data = json.load(g)
# print(type(result_data))
# # print(result_data[2])


# article_data =[]
# for n, each_article in enumerate(file_list):
#     article_path = source_file_path + '/' + each_article
#     with open(article_path, 'r', encoding = 'utf-8') as f:
#         tmp_article_string = f.read()
# print(tmp_article_string)