import os
import pickle
import threading
import numpy as np

# 主要配置两个路径即可，第一个是读取的jieba分完词后的dir
# 第二个是保存fit_params 的路径
resultdir = "D:/AAA/nlpdata/testJiebaClassFile"
writeFile = "D:/AAA/dataRefresh/turn1"
tfidftransformer_path = 'D:/AAA/nlpdata/tfidftransformer.pkl'
tfidftransformer = pickle.load(open(tfidftransformer_path, "rb"))

# fp = open('train_data2.txt','w',encoding="UTF-8")
# fp2 = open('test_data2.txt','w',encoding="UTF-8")

classList = ['phone','weather','translation','playcontrol','volume','FM',
             'limitLine','alarm','schedule','music','story','listenBook',
             'news','collect','musicinfo','healthAI','calculator','cookbook',
             'dictionary','joke','forex','stock','astrology','other']

arrList = tfidftransformer.get_feature_names()
def write_array(arr,f):
    writestrList = []
    for num_list in arr:
        writelinestr = ""
        for index in range(len(num_list)):
            if index == 0:
                writelinestr += str(int(num_list[index]))+" "
            else:
                if abs(num_list[index] - 0) > 1e-5:
                    writelinestr += str(index) + ":" + str(num_list[index])+" "
        writelinestr += '\n'
        writestrList.append(writelinestr)
    f.writelines(writestrList)

def write_array2(arr,filename):
    paramFilePath = os.path.join(writeFile,filename)
    with open(paramFilePath, 'a', encoding="UTF-8") as f:
        write_array(arr, f)


def writeOneClassToFile(jiebatxtpath,filename):
    with open(jiebatxtpath, encoding="UTF-8") as f:
        strList = f.readlines()
        strList = np.array(strList)
        # 下面按照每次500个数据去取,进行转换
        isLast = False
        nowIndex = 0
        while not isLast:
            if len(strList[nowIndex:]) < 500:
                isLast = True
                subArray = strList[nowIndex:]
            else:
                subArray = strList[nowIndex:nowIndex + 500]
                nowIndex += 500
            print(len(subArray))
            tfidfVector = np.array(tfidftransformer.transform(subArray).toarray())
            arr2 = np.array([classList.index(filename[:-4]) + 1])
            arr3 = np.insert(tfidfVector, 0, values=arr2, axis=1)
            predict_param = arr3
            write_array2(predict_param, filename)



list_file = os.listdir(resultdir)
list_file = sorted(list_file)
print(list_file)

threadList = []
for filename in list_file:
    jiebatxtpath = os.path.join(resultdir, filename)
    print(jiebatxtpath)
    t1 = threading.Thread(target=writeOneClassToFile,args=(jiebatxtpath,filename))
    threadList.append(t1)
for t in threadList:
    t.start()
    print('one thread start...')
for t in threadList:
    t.join()
print("all classes params write done...")
                # t1 = threading.Thread(target=write_array2, args=(predict_param, ))
                # t1.start()
                # t1.join()



