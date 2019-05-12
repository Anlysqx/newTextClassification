import os

classList = ['phone','weather','translation','playcontrol','volume','FM',
             'limitLine','alarm','schedule','music','story','listenBook',
             'news','collect','musicinfo','healthAI','calculator','cookbook',
             'dictionary','joke','forex','stock','astrology','other']

resultdir = "D:/AAA/nlpdata/testJiebaClassFile"

filelist = os.listdir(resultdir)
strList = []
for filename in filelist:
    if filename[:-4] not in classList:
        path = os.path.join(resultdir,filename)
        with open(path,encoding="UTF-8") as f:
            strList.extend(f.readlines())
        os.remove(path)
otherpath = os.path.join(resultdir,"other.txt")
with open(otherpath,encoding="UTF-8",mode='w') as f:
    for item in strList:
        f.write(item)