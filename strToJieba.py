import jieba
import os

print(" ".join(jieba.cut("我爱听刘德华的歌，你呢",cut_all=True)))

rootdir = "D:/AAA/nlpdata/classFile"
resultdir = "D:/AAA/nlpdata/jiebaClassFile"

list = os.listdir(rootdir)

for filename in list:
    path = os.path.join(rootdir,filename)
    with open(path,encoding="UTF-8") as f:
        strList = f.readlines()
        path2 = os.path.join(resultdir,filename)
        with open(path2,encoding="UTF-8",mode='w') as f2:
            for strItem in strList:
                f2.write(" ".join(jieba.cut(strItem.strip()))+'\n')



