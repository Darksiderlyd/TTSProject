
TrainTextFile = '西游记_白话文版.txt'

def amain():
    splitText('&#8195;;')

def splitText(splitSimp):

    with open(TrainTextFile, "r", encoding='utf-8') as text_file:
        text = text_file.read()
        splitted = text.split(splitSimp)



if __name__ == "__main__":
    amain()
