# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:53:41 2016

@author: Xian Guo
"""

import math
import string
import sys
import cProfile
#read .txt files
with open("book1.txt") as f:
    document1 = f.read()
with open("book2.txt") as f:
    document2 = f.read()
#change file into lines
def read_file(file):
    try:
        f = open(file,'r')
        return f.readlines()
    except IOError:
        print("Error opening reading input file:",file)
        sys.exit()

#get word from line list
def get_word_from_line_list(lines):
    wordList = []
    for L in lines:
        words_in_line = get_word_from_string(L)
        wordList = wordList + words_in_line
    return wordList
#get word from line
def get_word_from_string(line):
    wordList = []
    characterList = []
    for c in line:#遍历一行的每个字符
        if c.isalnum():
            characterList.append(c)
        elif len(characterList)>0:
            word="".join(characterList)
            word=word.lower()
            wordList.append(word)
            characterList=[]
    #处理只有一个word的情况
    if len(characterList)>0:
        word="".join(characterList)
        word=word.lower()
        wordList.append(word)
    return wordList
#计算word出现的频率
def count_frequency(wordList):
    L=[]
    for newWord in wordList:
        for entry in L:
            if(entry[0] == newWord):
                entry[1] = entry[1] + 1
                break
        else:
            L.append([newWord,1])
    return L
#对一个文件进行处理,返回出现的频率
def word_frequency_for_file(file):
    lineList = read_file(file)
    wordList = get_word_from_line_list(lineList)
    freq_map = count_frequency(wordList)
    return freq_map
#计算文件间的内积
def inner_product(L1,L2):
    sum = 0.0
    for word1,count1 in L1:
        for word2,count2 in L2:
            if(word1==word2):
                sum += count1*count2
    return sum
#计算文件之间的角度
def vector_angle(L1,L2):
    numerator=inner_product(L1,L2)
    denominator=math.sqrt(inner_product(L1,L1)+inner_product(L2,L2))
    return math.acos(numerator/denominator)

#计算文件距离
def doc_dist(d1,d2):
    sorted_word_list_1 = word_frequency_for_file(d1)
    sorted_word_list_2 = word_frequency_for_file(d2)
    distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
    return distance


#Optimization 1: remove list concatenation
def get_word_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_word_from_string(line)
        word_list.extend(words_in_line)
        return word_list
    
#Various smaller optimizations
# global variables needed for fast parsing
# translation table maps upper case to lower case and punctuation to spaces
translation_table = string.maketrans(string.punctuation+string.uppercase,
                                     " "*len(string.punctuation)+string.lowercase)

def get_words_from_text(text):
    """
    Parse the given text into words.
    Return list of all words found.
    """
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list

def count_frequency(word_list):
    """
    Return a dictionary mapping words to frequency.
    """
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D

def word_frequencies_for_text(text):
    """
    Return dictionary of (word,frequency) pairs for the given file.
    """
    word_list = get_words_from_text(text)
    freq_mapping = count_frequency(word_list)
    return freq_mapping

def inner_product(D1,D2):
    """
    Inner product between two vectors, where vectors
    are represented as dictionaries of (word,freq) pairs.

    Example: inner_product({"and":3,"of":2,"the":5},
                           {"and":4,"in":1,"of":1,"this":2}) = 14.0 
    """
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

def vector_angle(D1,D2):
    """
    The input is a list of (word,freq) pairs, sorted alphabetically.

    Return the angle between these two vectors.
    """
    numerator = inner_product(D1,D2)
    denominator = math.sqrt(inner_product(D1,D1)*inner_product(D2,D2))
    return math.acos(numerator/denominator)    
    
    
    
    
    
    
    

        
    
    
    
    
    
    
    
    
    
    
        