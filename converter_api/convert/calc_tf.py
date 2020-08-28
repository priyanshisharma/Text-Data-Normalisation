import string
import itertools
from pathlib import Path
import re
from collections import Counter
import operator
import pandas as pd
import pdftotext

'''
Below are some functions required for tf-idf scoring
'''

def Convert(tup):
    '''This function coverts a tuple to a dictionary'''
    di = dict()
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


def computeTF(wordDict, bow):
    '''This function returns the term frequency of the word'''
    tfDict = dict()
    bowCount = len(bow)
    for word,count in wordDict.items():
        tfDict[word] = count[0]/float(bowCount)

    return tfDict

def computeIDF(docList):
    '''This function returns the inverse document
    frequency of the word'''
    import math
    idfDict = dict()
    N = len(docList)

    #counts the number of documents that contain a word W
    #idfDict = dict.fromkeys(docList[0].keys(),0)
    idfDict = dict()
    for doc in docList:
        for word, val in doc.items():
            if val[0] > 0:
                try:
                    idfDict[word] += 1
                except:
                    idfDict[word] = 1

    #Divide N by denominator above, take the log of that
    for word, val in idfDict.items():
        idfDict[word]=math.log(N/float(val))

    return idfDict

def computeTFIDF(tfBow, idfs):
    '''This function returns the tf-idf score'''
    tfidf = dict()
    for word, val in tfBow.items():
        try:
            tfidf[word] = val*idfs[word]
        except:
            tfidf[word] = val*1
    return tfidf

'''Creating stopwords'''

stop_words = [ 'ourselves', 'hers', 'between', 'yourself', 'but',
'again', 'there', 'about', 'once', 'during', 'out', 'very',
'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do',
'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off',
'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his',
'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this',
'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to',
'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them',
'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves',
'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not',
'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only',
'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if',
'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was',
'here', 'than', 'I', 'also', ' ']

for symbol in string.punctuation:
    stop_words.append(symbol)

for num in range(2030):
    stop_words.append(str(num))

'''Required data members'''
tokenised_text = []
all_lines = str() #This will contain our overall data

p = Path('LinkedInProfiles/')

'''Removing stopwords and tokenising'''
for item in p.glob('*'): #Iterating through all the files in the path

    if str(item)=='LinkedInProfiles/.DS_Store':
        continue

    with open(str(item), 'rb') as pdf_file:
        pdf = pdftotext.PDF(pdf_file)

    pdf_lines = str() # This will contain each individual pdf

    for page in pdf:
        pdf_lines += str(page)

    lines_temp = re.split('\W+', str(pdf_lines)) #Tokenising

    filtered_sentence = []
    for word in lines_temp:
        if word not in stop_words: #Removing stop words
            filtered_sentence.append(word)

    tokenised_text.append(filtered_sentence)


'''Finding tf-idf score'''
_idfs_tokenised_text = [] #This shall contain the words and respective frequencies

#Finding frequency of all elements of each document
for text in tokenised_text:
    _idfs_tokenised_text.append(convert(Counter(text).most_common()))

#Compute total number of documents containing specific words
idfs = computeIDF(_idfs_tokenised_text)

