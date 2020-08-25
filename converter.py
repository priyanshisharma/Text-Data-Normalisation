import pdftotext
import pandas as pd
from pathlib import Path

dt = str() #This will contain our overall data
p = Path('LinkedInProfiles/')

for item in p.glob('*'): #Iterating through all the files in the path

    if(str(item)=='LinkedInProfiles/.DS_Store'):
        continue
    
    with open(str(item), 'rb') as pdf_file:
        pdf = pdftotext.PDF(pdf_file)

    lines = str() # This will contain each individual pdf

    for page in pdf:
        lines += str(page)
    
    '''
    CHOICE OF DELIMITTER
    I have used the dollar symbol assuming that there is a lesser chance
    of someone using this at in between their LinkedIn profile, which could
    otherwise cause undesired separation.
    '''
    dt += lines + '$' #Add delimitter


dt = dt.strip().split('$') #Split data to make a dataframe
res = pd.DataFrame(dt)
res.to_csv("task_2.csv")
