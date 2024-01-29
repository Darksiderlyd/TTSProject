# -*- coding: utf-8 -*-
import os
import shutil

from loguru import logger
import tempfile
from os.path import basename, splitext, exists, join
from mobi.kindleunpack import unpackBook

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录
project_root = os.path.abspath(os.path.join(current_dir, ".."))


def extract2(infile, userOutFile):
    """Extract mobi file and return path to epub file"""

    tempdir = tempfile.mkdtemp(dir=current_dir, prefix="mobiex")
    if hasattr(infile, "fileno"):
        tempname = next(tempfile._get_candidate_names()) + ".mobi"
        pos = infile.tell()
        infile.seek(0)
        with open(join(tempdir, tempname), "wb") as outfile:
            shutil.copyfileobj(infile, outfile)
        infile.seek(pos)
        infile = join(tempdir, tempname)

    logger.debug("file: %s" % infile)
    fname_in = basename(infile)
    base, ext = splitext(fname_in)
    fname_out_epub = base + ".epub"
    fname_out_html = "book.html"
    fname_out_pdf = base + ".001.pdf"
    unpackBook(infile, tempdir, epubver="A")
    epub_filepath = join(tempdir, "mobi8", fname_out_epub)
    html_filepath = join(tempdir, "mobi7", fname_out_html)
    pdf_filepath = join(tempdir, fname_out_pdf)
    if exists(epub_filepath):
        shutil.copyfile(epub_filepath, userOutFile)
        return tempdir, epub_filepath
    elif exists(html_filepath):
        return tempdir, html_filepath
    elif exists(pdf_filepath):
        return tempdir, pdf_filepath
    raise ValueError("Coud not extract from %s" % infile)


if __name__ == "__main__":
    print(extract2("jiandie.mobi", "jiandie.epub"))
