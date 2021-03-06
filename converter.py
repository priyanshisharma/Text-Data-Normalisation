'''This module uses set of pdf LinkedIn profile to produce frequency and importance of words in it'''
import itertools
from pathlib import Path
import re
from collections import Counter
import operator
import pandas as pd
import pdftotext
from tfidf import stop_words, computeIDF, computeTF,computeTFIDF,convert

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

    '''
    CHOICE OF DELIMITTER
    I have used the dollar symbol assuming that there is a lesser chance
    of someone using this at in between their LinkedIn profile, which could
    otherwise cause undesired separation.
    '''
    all_lines += pdf_lines + '$' #Add delimitter

    tokenised_text.append(filtered_sentence)


org_text = all_lines.strip().split('$') #Split data to separate profiles
org_text.pop() #removing final empty field that comes due to the '$' at end

'''Finding top 10 most occuring words'''
top_10_words_frequency = []
for text in tokenised_text:
    most_occur = Counter(text).most_common(10)
    top_10_words_frequency.append(most_occur)

'''Finding tf-idf score'''
_idfs_tokenised_text = [] #This shall contain the words and respective frequencies

#Finding frequency of all elements of each document
for text in tokenised_text:
    _idfs_tokenised_text.append(convert(Counter(text).most_common()))

#Compute total number of documents containing specific words
idfs = computeIDF(_idfs_tokenised_text)

top_10_words_importance = []
for text in tokenised_text:
    count = convert(Counter(text).most_common()) #Get frequency of word in text
    tf = computeTF(count,text) #Get tf values for word
    tfidf =  computeTFIDF(tf,idfs) #Get tf-idf value of word
    # Sort the words in descending order of importance
    sorted_d = dict(sorted(tfidf.items(), key=operator.itemgetter(1),reverse=True))
    #Retrieve the top 10 most important words
    most_important = dict(itertools.islice(sorted_d.items(), 10))
    top_10_words_importance.append(most_important)

'''Create the dataframe to be converted to csv file'''
res = pd.DataFrame()
res['Original Text'] = org_text
res['Tokenised Text'] = tokenised_text
res['10 most occuring words and their frequency'] = top_10_words_frequency
res['10 most important words and their tfidf score'] = top_10_words_importance

'''Create the csv file'''
res.to_csv("task.csv")
