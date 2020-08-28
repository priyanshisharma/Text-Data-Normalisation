'''Below are functions required for tf-idf scoring'''
import string

def convert(tup):
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
        tfidf[word] = val*idfs[word]
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
