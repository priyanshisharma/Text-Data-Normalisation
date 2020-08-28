# Text-Data-Normalisation
This is done according to the Screening Test of Code Vector

## Task 1
* Completed the download of 50 LinkedIn profiles, that are saved in the `LinkedInProfiles` folder of the repository.

<br/><br/>

**`converter.py`** contains the script for task 2,3. 
## Task 2
* Extracted the text from the first line and saved it in the first column of the task file

## Task 3
* Extracted 10 most frequently used words from every profile's data, excluding stopwords.
* Used tf-idf to scoring methodology to score every word, and return the 10 most important words(excluding stopwords) i.e. words with highest tfidf score, where tfidf - term frequency & Inverse document frequency.

Functions curated for tfidf implementation have been extracted to `tfidf.py`.
Install the `requirements.txt` in your environment and Run `python converter.py` to generate the required task file. The code has been commented for explanation.

<br/><br/>

## Task 4
I have used Django REST Framework to make the API. Navigate to the django project `converter_api` for accessing the same. The django app `convert` contains the required APIs.
Run `python manage.py runserver` to use it in your local server. Make sure you have installed the requirements.

* At `'pdf_to_text/'` there exists the api which takes `pdf_file` in the input and returns the `text` within it as output.
* At `'text_to_info/'` there exists the api which takes `text` as input and returns **the top 10 most frequent** words, and **the top 10 most important words** in that piece of text.

For important words I have used only **term frequency** i.e. (total occurences of the word/total words) and not **inverse document frequency**. The reason for doing the same is that;
* Term Frequency - Local Importance
* Inverse Document Frequency - Global Importance

Since, the text is not necessarily a part of a set of documents, its "global importance" becomes less relevant (not much to compare with), hence I am using term-frequency only.
