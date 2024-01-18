import asyncio
import os
import re
import string

from ttssrtvtt import batch_convert_vtt_to_srt

StartMultiArticleDic = 'startTexts'
SingleArticleText = 'texts'
VttDic = 'vtts'
SrtDic = 'srts'


# 读文件 DONE
# 划分多少章 DONE
# 按章写入文件 DONE
# 对输出文件夹进行ttsfile 输出语音和字幕文件

def getSingleArticleFile(file_name, multiFileName) -> string:
    return f"{SingleArticleText}/{multiFileName}-{file_name}.txt"


def splitMultiArtical(text, multiFileName) -> None:
    split_regex = r'第[一二三四五六七八九十百千万亿零0-9]+章\s+[^\n]+'

    print(text)

    subtexts = re.split(split_regex, text)
    titles = re.findall(split_regex, text)

    print(titles)
    print(subtexts)

    for i in range(len(titles)):
        print("{}\n{}".format(titles[i].strip(), subtexts[i + 1].strip()))
        with open(getSingleArticleFile(titles[i].strip(), multiFileName), "w", encoding="utf-8") as file:
            file.write(titles[i].strip())
            file.write('\n')
            file.write('　　')
            lines = subtexts[i + 1].strip()
            for line in lines:
                file.write(line)


def convertMultiArticalToSingle(text, file_name) -> None:
    splitMultiArtical(text, file_name)


def amain():
    # 创建输出文件夹
    if not os.path.exists(SingleArticleText):
        os.makedirs(SingleArticleText)

    # 遍历输入文件夹
    for root, dirs, files in os.walk(StartMultiArticleDic):
        for file in files:
            # 将文件中的文本读出来
            with open(os.path.join(root, file), "r", encoding='utf-8') as text_file:
                text = text_file.read()
                # 获取文件名
                file_name, ext = os.path.splitext(file)
                # 加入任务列表
                convertMultiArticalToSingle(text, file_name)


if __name__ == "__main__":
    amain()
