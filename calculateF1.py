import os
from sklearn.metrics import f1_score
import collections

path = 'C:/Users/mili/Desktop/f1/'
filelist = os.listdir(path)

classList = ['phone','weather','translation','playcontrol','volume','FM',
             'limitLine','alarm','schedule','music','story','listenBook',
             'news','collect','musicinfo','healthAI','calculator','cookbook',
             'dictionary','joke','forex','stock','astrology','other']


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

dirct = collections.defaultdict(int)
for i in origin:
    dirct[classList[i-1]] += 1
print(dirct)


labels = [i for i in range(1,len(classList)+1,1)]
print(labels)

print("预测样本数目 = ",len(origin))
print("f1_score(根据样本数加权平均值)  = ",f1_score(origin,predict,average="weighted"))
print("f1_score(未加权平均值)  = ",f1_score(origin,predict,average="macro"))
score_list = f1_score(origin,predict,labels=labels,average=None)

for i in range(0,24,1):
    print(classList[i],"\t\t--- ","数据占比: ",dirct[classList[i]]/len(origin),"\t\t--- F1: ",score_list[i])



