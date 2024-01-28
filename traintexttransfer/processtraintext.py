import re

TrainTextFile = 'traintext.txt'
TrainTextFileProcessed = 'traintextProcessed.txt'


def replace_placeholders(input_string):
    pattern = re.compile(r'#\d+|#X')  # 匹配类似#1、#2、#3、#X的字符串
    result = re.sub(pattern, '', input_string)
    return result


def amain():
    with open(TrainTextFile, "r", encoding='utf-8') as text_file:
        text = text_file.read()

        # 获取文件名
        with open(TrainTextFileProcessed, "w", encoding="utf-8") as file:

            lines = text.splitlines()
            i = 0
            for line in lines:
                if i % 2 == 0:
                    file.write(replace_placeholders(line[7:]))
                    file.write('\n')

                i = i + 1

                # if i == 4:
                #     break


if __name__ == "__main__":
    amain()
