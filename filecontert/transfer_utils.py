from filecontert.extract2 import extract2
from epub2txt import epub2txt
import subprocess

from filecontert.kindle.txt2epub2 import Txt2Epub2

mobi_file_path = 'jiandie.mobi'
epub_file_path = 'jiandie.epub'
txt_file_path = 'jiandie.txt'

mobi_file_out_path = 'jiandie_out.mobi'
epub_file_out_path = 'jiandie_out.epub'
txt_file_out_path = 'jiandie_out.txt'


def mobi_to_epub(mobi_file_path, epub_file_path):
    try:
        tempdir, filepath = extract2(mobi_file_path, epub_file_path)
        print('tempdir: ' + tempdir + '\nfilepath: ' + filepath + '\n')

        print("转换完成。")

    except Exception as e:
        print(f"发生错误: {str(e)}")


def txt_to_epub(txt_file_path, epub_file_path):
    txt2epubObj = Txt2Epub2(book_identifier='123123', book_title='剑谍', book_author='牛语者', book_language='zh-cn')
    txt2epubObj.create_epub(input_file=txt_file_path, output_file=epub_file_path)


def epub_to_txt(epub_file_path, txt_file_path):
    try:
        # from a url to epub
        # url = "https://github.com/ffreemt/tmx2epub/raw/master/tests/1.tmx.epub"
        # res = epub2txt(url)

        # from a local epub file
        # filepath = r"tests\test.epub"
        res = epub2txt(epub_file_path)

        # output as a list of chapters
        # ch_list = epub2txt(epub_file_path, outputlist=True)
        with open(txt_file_path, 'w', encoding='utf-8') as file:
            file.write(res)

        print("转换完成。")
    except Exception as e:
        print(f"发生错误: {str(e)}")


def epub_to_mobi(epub_file_path, mobi_file_path):
    try:
        subprocess.call(["ebook-convert", epub_file_path, mobi_file_path])
    except Exception as e:
        print(e)


def test():
    mobi_to_epub(mobi_file_path, epub_file_path)
    epub_to_txt(epub_file_path, txt_file_out_path)


if __name__ == "__main__":
    test()
