#!/bin/python
import sys
import re
import shutil
import os

split_by_book = re.compile("\n\-\-\-\sBook\s[0-9]+\s\-\-\-\n").split

whole_text = open(sys.argv[1], encoding='utf-8').read()

text_by_book = split_by_book(whole_text)

if os.path.isdir('the_odyssey'):
    shutil.rmtree('the_odyssey')

os.mkdir('the_odyssey')

for index, book in enumerate(text_by_book):
    path = 'the_odyssey/book-' + str(index + 1) + '.txt'
    file_to_write = open(path, 'a')
    file_to_write.write(book)
    file_to_write.close()
    print('Wrote file ' + path)
