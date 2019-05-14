import os
from sklearn.metrics import f1_score

path = 'C:/Users/mili/Desktop/f1/'
filelist = os.listdir(path)

origin = []
predict = []
with open(path+'test_data2.predict') as f:
    strLines = f.readlines()
    for strline in strLines:
        predict.append(int(strline.strip()))
    print(len(predict))

with open(path+'test_data2.txt') as f:
    strLines = f.readlines()
    for strline in strLines:
        origin.append(int(strline.split(' ')[0]))
    print(len(origin))

print("预测样本数目 = ",len(origin))
print("f1_score(根据样本数加权平均值)  = ",f1_score(origin,predict,average="weighted"))
print("f1_score(未加权平均值)  = ",f1_score(origin,predict,average="macro"))