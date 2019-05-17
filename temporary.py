import os
import pandas as pd

dirpath = 'D:/AAA/nlpdata/turn1'
resultdir = "D:/AAA/nlpdata/testJiebaClassFile"
writeFile = "D:/AAA/extractfile"
classList = ['phone','weather','translation','playcontrol','volume','FM',
             'limitLine','alarm','schedule','music','story','listenBook',
             'news','collect','musicinfo','healthAI','calculator','cookbook',
             'dictionary','joke','forex','stock','astrology','other']



filenames = os.listdir(dirpath)
# print(filenames)

txtlist = []
predictlist = []

for filename in filenames:
    if filename.endswith(".txt"):
        txtlist.append(filename)
    if filename.endswith('.predict'):
        predictlist.append(filename)

def writeToFile(sameLineClass,notSameLineClass,originalClass,errPredictClass,txtfilename):
    originalClass = [item+'\n' for item in originalClass]
    errPredictClass = [item+'\n' for item in errPredictClass]
    with open(os.path.join(writeFile,txtfilename),encoding="UTF-8",mode='a') as f:
        f.writelines(sameLineClass)
    with open(os.path.join(writeFile,"err.txt"),encoding="UTF-8",mode='a') as f:
        f.writelines(notSameLineClass)
    with open(os.path.join(writeFile,"originalClass.txt"),encoding="UTF-8",mode='a') as f:
        f.writelines(originalClass)
    with open(os.path.join(writeFile,"errPredictClass.txt"),encoding="UTF-8",mode='a') as f:
        f.writelines(errPredictClass)

def writeToCsv():
    write_csv = "errClassFile.csv"
    # 处理待存数据为list结构
    errList = []
    originalClass = []
    errPredictClass = []
    with open("D:/AAA/extractfile/err.txt",encoding="UTF-8",mode='r') as f:
        errList.extend(f.readlines())
    with open("D:/AAA/extractfile/originalClass.txt",encoding="UTF-8",mode='r') as f:
        originalClass.extend(f.readlines())
    with open("D:/AAA/extractfile/errPredictClass.txt",encoding="UTF-8",mode='r') as f:
        errPredictClass.extend(f.readlines())
    column_errList = pd.Series(errList, name='errList')
    column_originalClass = pd.Series(originalClass, name='originalClass')
    column_errPredictClass = pd.Series(errPredictClass, name='errPredictClass')
    con = pd.concat([column_errList,column_originalClass,column_errPredictClass], axis=1)
    con.to_csv(write_csv, index=False,encoding="UTF-8")



for predictfile in predictlist:
    classNum = classList.index(predictfile[:-8])+1
    txtfilename = predictfile[:-8]+".txt"
    strLines = []
    with open(os.path.join(resultdir,txtfilename),encoding="UTF-8") as f:
        strLines.extend(f.readlines())

    with open(os.path.join(dirpath,predictfile)) as f:
        numlines = f.readlines()
        notSameLineClass = []
        sameLineClass = []
        originalClass = []
        errPredictClass = []
        for onenum_index in range(len(numlines)):
            onenum = numlines[onenum_index]
            onenum = int(onenum.strip())
            if onenum != classNum:
                notSameLineClass.append(strLines[onenum_index])
                originalClass.append(predictfile[:-8])
                errPredictClass.append(classList[onenum-1])
            else:
                sameLineClass.append(strLines[onenum_index])
        writeToFile(sameLineClass,notSameLineClass,originalClass,errPredictClass,txtfilename)
writeToCsv()

