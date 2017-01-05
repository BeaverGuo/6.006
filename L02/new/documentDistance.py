# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:53:41 2016

@author: Xian Guo
"""

import math
import string
import sys
import cProfile
#read file book1.txt and book2.txt
with open("book1.txt") as f:
    document1 = f.read()
with open("book2.txt") as f:
    document2 = f.read()


# useage: read_file("book1.txt")
def read_file(filename):
    """ 
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    """
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print "Error opening or reading input file: ",filename
        sys.exit()
'''
def get_words_from_line_list(L):
    """
    Parse the given list L of text lines into words.
    Return list of all words found.
    """

    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list = word_list + words_in_line
    return word_list
'''

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



def word_frequencies_for_text(text):
    """
    Return dictionary of (word,frequency) pairs for the given file.
    """
    word_list = get_words_from_text(text)
    freq_mapping = count_frequency(word_list)
    return freq_mapping

#Optimization 1: remove list concatenation
def get_words_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list.extend(words_in_line)
        return word_list



def get_words_from_string(line):
    """
    Return a list of the words in the given input string,
    converting each word to lower-case.

    Input:  line (a string)
    Output: a list of strings 
              (each string is a sequence of alphanumeric characters)
    """
    word_list = []          # accumulates words in line
    character_list = []     # accumulates characters in word
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list)>0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list)>0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list

'''
#list in list (word,frequency)
def count_frequency(word_list):
    """
    Return a list giving pairs of form: (word,frequency)
    """
    L = [] #use a new list to cache, is dict a better choice?
    for new_word in word_list:
        for entry in L:
            if new_word == entry[0]:
                entry[1] = entry[1] + 1
                break
        else:
            L.append([new_word,1])
    return L
'''

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

'''
def word_frequencies_for_file(filename):
    """
    Return alphabetically sorted list of (word,frequency) pairs 
    for the given file.
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    return freq_mapping # [[word0, freq0]...]
'''

'''
def inner_product(L1,L2):
    """
    Inner product between two vectors, where vectors
    are represented as lists of (word,freq) pairs.

    Example: inner_product([["and",3],["of",2],["the",5]],
                           [["and",4],["in",1],["of",1],["this",2]]) = 14.0 
    """
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum += count1 * count2
    return sum
'''
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




def vector_angle(L1,L2):
    """
    The input is a list of (word,freq) pairs, sorted alphabetically.

    Return the angle between these two vectors.
    """
    numerator = inner_product(L1,L2)
    denominator = math.sqrt(inner_product(L1,L1)*inner_product(L2,L2))
    return math.acos(numerator/denominator) # math.acos good!

def document_distance(d1, d2):
    sorted_word_list_1 = word_frequencies_for_text(d1)
    
    sorted_word_list_2 = word_frequencies_for_text(d2)
    distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
    return distance


distance = document_distance("book2.txt", "book1.txt")
distance1 = document_distance("book1.txt", "book1.txt")
print "The distance between the documents is: %0.6f (radians)"% distance,
print "The distance1 between the documents is: %0.6f (radians)"% distance1
