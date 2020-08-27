import pdftotext
import pandas as pd
from pathlib import Path
import re
from collections import Counter 
import string 


tokenised_text = [] 
all_lines = str() #This will contain our overall data
p = Path('LinkedInProfiles/')

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
'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 
'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', 'I', 'also']

for symbol in string.punctuation:
    stop_words.append(symbol)

for num in range(100):
    stop_words.append(str(num))


for item in p.glob('*'): #Iterating through all the files in the path

    if(str(item)=='LinkedInProfiles/.DS_Store'):
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


org_text = all_lines.strip().split('$') #Split data to make a dataframe
org_text.pop() #removing final empty field that comes due to the '$' at end

'''Finding top 10 most occuring words'''
top_10_words = []
for text in tokenised_text:
    most_occur = Counter(text).most_common(10)
    top_10_words.append(most_occur)

res = pd.DataFrame()
res['Original Text'] = org_text
res['Tokenised Text'] = tokenised_text
res['10 most occuring words and their frequency'] = top_10_words

res.to_csv("task.csv")
