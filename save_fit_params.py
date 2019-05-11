import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# 主要配置两个路径即可，第一个是读取的jieba分完词后的dir
# 第二个是保存fit_params 的路径
resultdir = "D:/AAA/nlpdata/testJiebaClassFile"
tfidftransformer_path = 'D:/AAA/nlpdata/tfidftransformer.pkl'

list_file = os.listdir(resultdir)

# 用于存放所有的文档字符串
fitlist = []

for filename in list_file:
    path = os.path.join(resultdir,filename)
    with open(path,encoding="UTF-8") as f:
        strList = f.readlines()
        fitlist.extend(strList)

vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", encoding="UTF-8")
vectorizer.fit(fitlist)

with open(tfidftransformer_path, 'wb') as fw:
    pickle.dump(vectorizer, fw)

