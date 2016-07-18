#!/bin/python
import csv
import re
import sys

split_by_n = re.compile("\n").split
has_full_stop = re.compile("\.").search
is_book_line = re.compile("\-\-\-\sBook\s[0-9]+\s\-\-\-").search

text = open(sys.argv[1], encoding='utf-8').read()
to_write = open(sys.argv[2], 'a')
fieldnames = ['line_no', 'book_line_no', 'sentence_no', 'book_no', 'line']
csv_writer = csv.DictWriter(to_write, fieldnames=fieldnames)
csv_writer.writeheader()

book_no = 0
sentence_no = 1
line_no = 1

for line in split_by_n(text):
    if is_book_line(line):
        book_no += 1
        sentence_no = 1
        continue

    if len(line.strip()) == 0:
        continue

    csv_writer.writerow({
        'book_line_no': re.sub("\-\-.+", "", line),
        'line_no': line_no,
        'sentence_no': sentence_no,
        'book_no': book_no,
        'line': re.sub("^[0-9]+\-\-\s", "", line)
    })

    if has_full_stop(line):
        sentence_no += 1

    line_no += 1


to_write.close()
