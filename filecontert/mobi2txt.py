import mobi
import html2text

filename = "test.mobi"
tempdir, filepath = mobi.extract(filename)
file = open(filepath, "r")
content = file.read()
print(html2text.html2text(content))
