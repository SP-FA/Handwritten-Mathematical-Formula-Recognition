import os
import shutil

path = r"E:\Computer\AI\scientific_research\surf-2022-6\data\ourData\seq"

picList = os.listdir(path)
label = []

fp = open('../data/seq.txt', mode='a')

id = 75604

for i in range(id, id + len(picList)):
    name = picList[i - id].split("_")[0].replace(" ", "").replace("#", "\\")
    label.append("(" + str(i) + ").jpg " + name + "\n")
    shutil.copy(os.path.join(path, picList[i - id]), os.path.join("../data/data/images", "(" + str(i) + ").jpg"))

fp.writelines(label)
fp.close()
