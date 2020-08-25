import pdftotext
import pandas as pd

dt = str()

for i in range(1,51):
    with open(('LinkedInProfiles/'+str(i)+'.pdf'), 'rb') as pdf_file:
        pdf = pdftotext.PDF(pdf_file)

    lines = str()

    for page in pdf:
        lines += str(page)
    
    dt += lines + '$'


dt = dt.strip().split('$')
res = pd.DataFrame(dt)
res.to_csv("task_2.csv")
