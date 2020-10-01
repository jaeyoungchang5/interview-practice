#!/usr/bin/env python3
import re # REGEX

words_dict = {} # initialize dictionary
sentence = input().lower() # take input & convert all alphabetical characters to lowercase

# Split up sentence into individual words
for word in sentence.split():
    word = re.sub('[^A-Za-z0-9]', '', word.strip()) # delete non-alphanumeric characters from words 
    words_dict[word] = words_dict.get(word, 0) + 1 # increment word frequency

### SORT ###
words_dict = {key: val for key, val in sorted(words_dict.items(), key=lambda word: word[0])} # alphabetic sort (ascending)
words_dict = {key: val for key, val in sorted(words_dict.items(), key=lambda word: word[1], reverse=True)} # frequency sort (descending)

### OUTPUT ###
for key, val in words_dict.items():
    print(key, val)
