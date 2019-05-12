import os
import pickle
import threading

import numpy as np

# 主要配置两个路径即可，第一个是读取的jieba分完词后的dir
# 第二个是保存fit_params 的路径
resultdir = "D:/AAA/nlpdata/testJiebaClassFile"
tfidftransformer_path = 'D:/AAA/nlpdata/tfidftransformer.pkl'
tfidftransformer = pickle.load(open(tfidftransformer_path, "rb"))
fp = open('train_data.txt','w')
fp2 = open('test_data.txt','w')

classList = ['phone','weather','translation','playcontrol','volume','FM',
             'limitLine','alarm','schedule','music','story','listenBook',
             'news','collect','musicinfo','healthAI','calculator','cookbook',
             'dictionary','joke','forex','stock','astrology','other']


def write_array(arr,f):
    for num_list in arr:
        for index in range(len(num_list)):
            if index == 0:
                f.write(str(int(num_list[index])))
                f.write(" ")
            else:
                if num_list[index] - 0 > 1e-5:
                    f.write(str(index) + ":" + str(num_list[index]))
                    f.write(" ")
        f.write('\n')



list_file = os.listdir(resultdir)
list_file = sorted(list_file)
print(list_file)

train_data = []
test_data = []
for filename in list_file:
    path = os.path.join(resultdir,filename)
    with open(path,encoding="UTF-8") as f:
        if filename == "poem.txt":
            strList = f.readlines()
            strList = np.array(strList)
            np.random.shuffle(strList)
            strList = np.array(tfidftransformer.transform(strList).toarray())
            arr2 = np.array([list_file.index(filename) + 1])
            arr3 = np.insert(strList, 0, values=arr2, axis=1)
            train_data = np.array(arr3[:int(len(arr3) * 0.7)])
            test_data = np.array(arr3[int(len(arr3) * 0.7):])
            threading.Thread(target=write_array, args=(train_data, fp)).start()
            threading.Thread(target=write_array, args=(test_data, fp2)).start()
            del train_data
            del test_data


# 现在 dict[key]里面保存的是每一行第一列是类别，其他列是tfidf特征,已经是l2缩放过了
# 按0.7 0.3比例取训练集和测试集，按照libsvm的格式输出到两个文件中就可以了


