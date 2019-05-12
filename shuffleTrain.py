import os
import numpy as np

path = "D:/NLP_SOUNDAI/textClassfic2/readData/export/train_data2.txt"
savepath = "D:/NLP_SOUNDAI/textClassfic2/readData/export/train_data_shuffle.txt"

with open(path,encoding="UTF-8") as f:
    patternList = f.readlines()
    patternList = np.array(patternList)
    np.random.shuffle(patternList)
    with open(savepath,encoding="UTF-8",mode='w') as fp:
        fp.writelines(patternList)
