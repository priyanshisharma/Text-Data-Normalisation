import pdftotext
import pandas as pd
from pathlib import Path
import nltk.data
import re

tokenizer = nltk.data.load('english.pickle') 

dt = str() #This will contain our overall data
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
'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

for item in p.glob('*'): #Iterating through all the files in the path

    if(str(item)=='LinkedInProfiles/.DS_Store'):
        continue
    
    with open(str(item), 'rb') as pdf_file:
        pdf = pdftotext.PDF(pdf_file)

    lines = str() # This will contain each individual pdf

    for page in pdf:
        lines += str(page)
    
    filtered_sentence = str()

    lines_temp = re.split('\W+', str(lines))
    
    for word in lines_temp:
        if word not in stop_words:
            filtered_sentence += (str(str(word)+' '))
    
    '''
    CHOICE OF DELIMITTER
    I have used the dollar symbol assuming that there is a lesser chance
    of someone using this at in between their LinkedIn profile, which could
    otherwise cause undesired separation.
    '''
    dt += filtered_sentence + '$' #Add delimitter


dt = dt.strip().split('$') #Split data to make a dataframe
res = pd.DataFrame(dt)
res.to_csv("task_3.csv")
