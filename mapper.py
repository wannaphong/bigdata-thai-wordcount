
# -*- coding: utf-8 -*-
"""mapper.py
fork from https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
"""
from pythainlp.tokenize import word_tokenize
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = word_tokenize(line)
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word, 1))
