#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 情感分类的步骤：
# 1、数据预处理
# 2、分词
# 3、提取特征
# 4、训练
# 5、测试
# 6、分析数据
#

# # 体验

# In[1]:
from snownlp import SnowNLP

# In[2]:
text = "这个菜有点难吃。谁也不想吃。"
s = SnowNLP(text)
print(text, s.sentiments)

t2 = "这首歌真难听"
s = SnowNLP(t2)
print(t2, s.sentiments)

t2 = "今天天气真好啊"
s = SnowNLP(t2)
print(t2, s.sentiments)

# # 训练测试

# 准备消极和积极情感的文本，分别为neg.txt和pos.txt

# ## 训练

from snownlp import sentiment
sentiment.train('neg.txt', 'pos.txt')
sentiment.save("sentiment.marshal")

# 将训练好的模型sentiment.marshal放到软件snownlp工具包安装路径下

t2 = "这首歌真难听"
s = SnowNLP(t2)
print(t2, s.sentiments)

t2 = "今天天气真好啊"
s = SnowNLP(t2)
print(t2, s.sentiments)


#准确率
import pandas as pd
import numpy as np
data_test = pd.read_excel("test.xlsx")
data_test.head()

s = []
for c in data_test['comment']:
    score = SnowNLP(c).sentiments
    if score>=0.5:
        s.append(1)
    else:
        s.append(0)
count = np.sum((s == data_test['sentiment'])==1)
print('准确率为：',count/len(data_test))


# # 分析数据

data = pd.read_excel("data.xlsx")
print(data.head())



# In[17]:


s = []
for c in data['comment']:
    score = SnowNLP(c).sentiments
    if score>=0.5:
        s.append(1)
    else:
        s.append(0)
data['sentiment'] = s
print(data.head())



# In[18]:


data.to_excel("data_result.xlsx",index=False)


# In[ ]:




