import re

text = '''第四十一章 留言夜出
　　韩立可没有这么长的时间可以苦侯，最多再过四五个月，墨大夫就会和他彻底摊牌，他必须在此之前拥有一定的自保能力。
第四十二章 云翅鸟
　　“你太得意忘形了，这小子精明的很，不是个省油的灯。你别眼看大功告成，却功亏一篑，载在了这个小子手里。”突然间另一青年男子的声音，在墨大夫脑中响起。
　　'''

split_regex = r'第[一二三四五六七八九十百千万亿零0-9]+章\s+[^\n]+'

subtexts = re.split(split_regex, text)
titles = re.findall(split_regex, text)

print(titles)

for i in range(len(titles)):
    print("{}\n{}".format(titles[i].strip(), subtexts[i + 1].strip()))
    #TODO 输出文件


