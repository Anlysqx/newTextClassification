import os

dirpath = r'D:\AAA\NEW_ONE_REFRESH\NEW_extractfile_3'

trainList = []
testList = []
validateList = []

fileNames = os.listdir(dirpath)

for filename in fileNames:
    with open(os.path.join(dirpath,filename),encoding="UTF-8") as f:
        cat_name = filename[:-4]
        allLines = f.readlines()
        allLines = [cat_name+'\t'+"".join(item.split(' ')) for item in allLines]
        trainList.extend(allLines[:int(len(allLines)*0.7)])
        validateList.extend(allLines[int(len(allLines)*0.7):int(len(allLines)*0.8)])
        testList.extend(allLines[int(len(allLines)*0.8):])

print(len(trainList))
print(len(testList))
print(len(validateList))

with open('data/cnews.train.txt',encoding="UTF-8",mode='a') as f:
    f.writelines(trainList)

with open('data/cnews.test.txt',encoding="UTF-8",mode='a') as f:
    f.writelines(testList)

with open('data/cnews.val.txt',encoding="UTF-8",mode='a') as f:
    f.writelines(validateList)