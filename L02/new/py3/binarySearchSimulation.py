#Binary search simulation
import numpy as np
from scipy.spatial.distance import cosine as cosine_similarity
import random
import cProfile
#execute cli: pip install numpy
#下面的python2会报错,python 3也要将unichr改成chr
def generated_ordered_cards():
    cards = []
    cards.extend(chr(x) for x in range(127185, 127185 + 14))
    cards.extend(chr(x) for x in range(127169, 127169 + 14))
    cards.extend(chr(x) for x in range(127153, 127153 + 14))    
    cards.extend(chr(x) for x in range(127137, 127137 + 14))
    return cards

print (generated_ordered_cards())


DOMAIN = generated_ordered_cards()
NUM_SAMPLES = 20 #随机取20张不重复的牌

class Problem(object):
    def __init__(self):
        self.elements = set()
        while len(self.elements) < NUM_SAMPLES:
            self.elements.add(random.choice(DOMAIN))
        self.elements = sorted(list(self.elements))
        self.hide_all()
        self.query = random.choice(self.elements)

    def ask(self, position):
        assert 0<=position<NUM_SAMPLES
        self.visible[position] = True
        return self

    def hide_all(self):
        self.visible = [False for _ in range(NUM_SAMPLES)]

    def _repr_html(self):
        els_html = []
        for el_idx in range(len(self.elements)):
            if self.visible[el_idx]:
                els_html.append("<td style='text-align:center'><font size='5'><b>%s</b></font></td>" % (self.elements[el_idx]))
            else:
                els_html.append("<td style='text-align:center;background:lightskyblue'<small><font color='grey'>%d</font></small></td>" % (el_idx,))
        header_html = u"<center><h1>Find %s! (♣ < ♦ < ♥ < ♠)</h1></center><br />" % (self.query,)
        table_html = "<table width='100%%' height='50px' style='table-layout: fixed'><tr>%s</tr></table>" % ("".join(els_html))
        return header_html + table_html

#Glove vectors

class Glove(object):
    def __init__(self,path):
        self.word_vector = []

        with open(path) as f:
            for line in f:
                if len(line) < 1:
                    break
                line = line.split(' ')
                word, vector = line[0], np.array(float(x) for x in line[1:])
                self.word_vector.append((word,vector))
        self.word_vector.sort()

    def __call__(self,key):
        return self.find_vector(key)

    def find_vector(self,key):
        for word,vector in self.word_vector:
            if word == key:
                return vector
        raise KeyError(key)

    def find_closest_word(self,key_vector,blacklist=[]):
        best_similarity = float('inf')
        best_word = None
        for word,vector in self.word_vector:
            if word in blacklist:
                continue
            similarity = cosine_similarity(vector,key_vector)
            if best_similarity > similarity:
                best_similarity = similarity
                best_word = word
        return best_word



#Implementation using binary search
def find_vector(self, key, lo=None, hi=None, debug=False):
    # Make sure by default we search over entire table
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(self.word_vector) - 1
    
    if lo > hi:
        raise KeyError(key)
    
    mid = (hi + lo) / 2
    word, vector = self.word_vector[mid]
    if debug:
        print("Looking for %s in range(%d, %d). Middle is %s" % (key, lo, hi, word))

    if word == key:
        return vector
    elif key < word:
        return self.find_vector(key, lo, mid - 1, debug=debug)
    else: # key > word
        return self.find_vector(key, mid + 1, hi, debug=debug)
    
Glove.find_vector = find_vector

