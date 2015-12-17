#! /usr/bin/python

import sys
import operator
from DictionaryServices import DCSCopyTextDefinition

file_name = sys.argv[1]
if len(sys.argv) > 2:
    known_words_file_name = sys.argv[2]
else:
    known_words_file_name = None

word_dic = dict()
word_trans = ''.join(chr(c) if chr(c).isupper() or chr(c).islower() else ' ' for c in range(256))
known_words = []

if known_words_file_name:
    for line in open(known_words_file_name):
        word = line.rstrip()
        known_words.append(word)


def get_words(line):
    line = line.translate(word_trans)
    return filter(lambda x: x != '', line.split(' '))


def lookup_word(word):
    word_range = (0, len(word))
    dict_result = DCSCopyTextDefinition(None, word, word_range)
    if not dict_result:
        err_msg = "'%s' not found in Dictionary." % (word)
        print err_msg.encode('utf-8')
    else:
        print dict_result.encode('utf-8')


for line in open(file_name):
    words = get_words(line)
    for word in words:
        word = word.lower()
        if word in word_dic:
            value = word_dic[word]
            word_dic[word] = value + 1
        else:
            word_dic[word] = 1

sorted_dic = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

counter = 0
for (key, value) in sorted_dic:
    if key not in known_words:
        print(str(counter) + ". " + key + ":\n")
        lookup_word(key)
        print("\n----------------------------------------------------------------\n")
        counter = counter + 1
