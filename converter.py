import pdftotext
import re
import csv
import pandas as pd
from pathlib import Path

dt = str()
p = Path('LinkedInProfiles/')
'''
for i in range(50):
    #print(i)
    #if(i==Path('LinkedInProfiles/.DS_Store')):
        #continue
    #print(p)
    a = Path(str('LinkedInProfiles/'+str(i)+'.pdf'))
    with open(a, 'rb') as pdf_file:
        pdf = pdftotext.PDF(pdf_file)

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'
'''

#for item in p.glob('*'):
for i in range(15):
    with open(('LinkedInProfiles/'+str(i)+'.pdf'), 'rb') as pdf_file:
        #print(i)
        pdf = pdftotext.PDF(pdf_file)
        pdf_file.close()

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'

for i in range(14,18):
    with open(('LinkedInProfiles/'+str(i)+'.pdf'), 'rb') as pdf_file:
        #print(i)
        pdf = pdftotext.PDF(pdf_file)
        pdf_file.close()

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'

for i in range(19,28):
    with open(('LinkedInProfiles/'+str(i)+'.pdf'), 'rb') as pdf_file:
        #print(i)
        pdf = pdftotext.PDF(pdf_file)
        pdf_file.close()

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'

for i in range(30,44):
    with open(('LinkedInProfiles/'+str(i)+'.pdf'), 'rb') as pdf_file:
        #print(i)
        pdf = pdftotext.PDF(pdf_file)
        pdf_file.close()

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'

for i in range(42,51):
    with open(('LinkedInProfiles/'+str(i)+'.pdf'), 'rb') as pdf_file:
        #print(i)
        pdf = pdftotext.PDF(pdf_file)
        pdf_file.close()

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'
    
dt = dt.strip().split('$')
#for i in range(50):
#    print('LinkedInProfiles/'+str(i)+'.pdf')

    


#for page in pdf:
#    print(page)

#print(len(pdf))

#lines = ((str(pdf[0])+str(pdf[1])) + '$' + (str(pdf2[0])+str(pdf2[1]))).strip().split('$')

#tx = ("\n".join(dt)).strip()

res = pd.DataFrame(dt)
res.to_csv("task_2.csv")
#print(res)


#for i in range(len(tx)):
#    print(str(i)+'    '+tx[i])

#print(lines[39])