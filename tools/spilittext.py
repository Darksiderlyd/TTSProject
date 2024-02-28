import os

TrainTextFile = '西游记_白话文版.txt'
FILE_RESULT = 'split'


def amain():
    splitText('&#8195;;')


def getChildFileName(file_name, index):
    return f"{FILE_RESULT}/{getSomeIndex(file_name, index)}.txt"


def getSomeIndex(file_name, index):
    return f"第{index}集  {file_name}"


def splitText(splitSimp):
    if not os.path.exists(FILE_RESULT):
        os.makedirs(FILE_RESULT)

    with open(TrainTextFile, "r", encoding='utf-8') as text_file:
        text = text_file.read()
        splitteds = text.split(splitSimp)
        # 获取文件名
        file_name, ext = os.path.splitext(TrainTextFile)

        for i in range(len(splitteds)):
            with open(getChildFileName(file_name, i), "w", encoding="utf-8") as file:
                file.write(getSomeIndex(file_name, i))
                file.write("\n")
                file.write(splitteds[i].strip())


if __name__ == "__main__":
    amain()
