from paddlespeech.cli.text.infer import TextExecutor

text_punc = TextExecutor()
result = text_punc(text="今天的天气真不错啊你下午有空吗我想约你一起去吃饭")
print(result)
