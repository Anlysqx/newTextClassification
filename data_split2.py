import os
import pickle
import threading
import numpy as np

# 主要配置两个路径即可，第一个是读取的jieba分完词后的dir
# 第二个是保存fit_params 的路径
resultdir = "D:/AAA/nlpdata/testJiebaClassFile"
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

def write_array2(arr,fstr,sub_arr):
    if fstr == "train":
        with open('train_data2.txt', 'a',encoding="UTF-8") as f:
            write_array(arr, f)
    elif fstr == "test":
        with open('test_data2.txt', 'a',encoding="UTF-8") as f:
            write_array(arr, f)






list_file = os.listdir(resultdir)
list_file = sorted(list_file)
print(list_file)

train_data = []
test_data = []

for filename in list_file:
    path = os.path.join(resultdir,filename)
    with open(path,encoding="UTF-8") as f:
            strList = f.readlines()
            strList = np.array(strList)
            np.random.shuffle(strList)
            # 下面按照每次500个数据去取,进行转换
            isLast = False
            nowIndex = 0
            while not isLast:
                if len(strList[nowIndex:]) < 500:
                    isLast = True
                    subArray = strList[nowIndex:]
                else:
                    subArray = strList[nowIndex:nowIndex+500]
                    nowIndex += 500
                print(len(subArray))
                tfidfVector = np.array(tfidftransformer.transform(subArray).toarray())
                arr2 = np.array([classList.index(filename[:-4]) + 1])
                arr3 = np.insert(tfidfVector, 0, values=arr2, axis=1)
                train_data = np.array(arr3[:int(len(arr3) * 0.7)])
                test_data = np.array(arr3[int(len(arr3) * 0.7):])
                str_sub_arr_train = np.array(subArray[:int(len(subArray) * 0.7)])
                str_sub_arr_test = np.array(subArray[:int(len(subArray) * 0.7)])
                t1 = threading.Thread(target=write_array2, args=(train_data, "train",str_sub_arr_train))
                t2 = threading.Thread(target=write_array2, args=(test_data, "test",str_sub_arr_test))
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                del train_data
                del test_data


# 现在 dict[key]里面保存的是每一行第一列是类别，其他列是tfidf特征,已经是l2缩放过了
# 按0.7 0.3比例取训练集和测试集，按照libsvm的格式输出到两个文件中就可以了


#
#
# arrList = tfidftransformer.get_feature_names()
#
#
# for filename in list_file:
#     path = os.path.join(resultdir,filename)
#     with open(path,encoding="UTF-8") as f:
#         if filename == "music.txt":
#             strList = f.readlines()
#             strList = np.array(strList)
#             np.random.shuffle(strList)
#             totalNum = len(strList)
#             conditionNum = 0
#             strList = ["嗯 播放 周华健 的 歌"]
#             for strline in strList:
#                 strline = np.array([strline.strip()])
#                 paramsVector = np.array(tfidftransformer.transform(strline).toarray())
#                 isallzero = True
#                 for num in paramsVector[0]:
#                     if abs(num - 0) > 1e-5:
#                         isallzero = False
#                         break
#                 if isallzero:
#                     print(strline,"是全0")
#                     conditionNum += 1
#                     print(strline)
#                 else:
#                     print("不是全0")
#
#             print("totalNum = ",totalNum)
#             print("conditionNum = ",conditionNum)
#
# print(arrList)


