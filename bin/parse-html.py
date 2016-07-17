#!/bin/python
from html.parser import HTMLParser
import sys
import re

is_line = re.compile("^<l[\s>]").match
is_book = re.compile("^<div1.+type=\"Book\"").match
is_milestone = re.compile("^<milestone").match
is_blank = re.compile("^\s*$").match

class MyHTMLParser(HTMLParser):
    line_no = 1
    bk_no = 1

    def handle_data(self, data):
        start_tag = str(self.get_starttag_text())

        if is_book(start_tag):
            sys.stdout.write('--- Book ' + str(self.bk_no) + ' ---\n')
            self.bk_no += 1
            self.line_no = 1

        if is_blank(data):
            return;

        if is_line(start_tag) or is_milestone(start_tag):
            sys.stdout.write(str(self.line_no) + '-- ' + data + '\n')
            self.line_no += 1

parser = MyHTMLParser()
odyssey_xhtml = open(sys.argv[1], encoding='utf-8').read()

parser.feed(odyssey_xhtml)
