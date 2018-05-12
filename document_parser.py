#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================================
# document_parser 
# Author: Eric Thomas
# Date: 5/11/2018
# Count total lines, words, specific word occurrences and top 3 words by frequency.
# ====================================================================================
# This program requires python 3.6.4.
# In a terminal window run:
# 1 python parser.py 
# 2 follow prompts
# ====================================================================================

def document_stats(filename, my_word):
    print("Processing file: " + filename)
    
    from collections import Counter
    import re
    
    my_word_count = 0
    total_words_count = 0
    c = Counter()
    
    #count a specific word and and 3 most common words in the file
    document = re.findall('\w+', open(filename).read().lower())
    most_common=(Counter(document).most_common(3))
    line_count = sum(1 for line in open(filename))           
    total_words = sum(c.values())
    for word in document:
       if word in my_word:
           my_word_count += 1
       total_words_count += 1
    
    #print results
    print("Line count: ", line_count)
    print("Total words in file:", total_words_count)
    print ("Count of the word:",my_word, my_word_count)
    print("Three most common words:") 
    for word, count in most_common: print('%s' % (word),)

def main():
    filename = input("file name path:")
    my_word = input("Which word would you like to count?")
    print("\033c")
    document_stats(filename, my_word)

main()