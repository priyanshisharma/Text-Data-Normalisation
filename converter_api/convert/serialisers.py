import operator
import itertools
import re
from collections import Counter
from rest_framework import serializers
import pdftotext
from .calc_tf import stop_words, Convert,computeTF, computeTFIDF, idfs

class ConvertFileSerialiser(serializers.Serializer):
    '''
    This serialiser takes pdf files as input and contains a
    function to retrieve the text from it.
    '''
    pdf_file = serializers.FileField()

    def conv(self):
        '''This function returns the text in the pdf file'''
        valid_data = self.validated_data
        try:
            pdf = pdftotext.PDF(valid_data["pdf_file"])
        except:
            raise serializers.ValidationError(
                {"file_type":"Please enter file with '.pdf' extension"}
            )

        pdf_lines = str()
        for page in pdf:
            pdf_lines += str(page)

        return pdf_lines


class ConvertTextSerialiser(serializers.Serializer):
    '''
    This serialiser takes text as input and contains a
    function to retrieve most frequent and important
    words from it.
    '''
    text = serializers.CharField()

    def most_occ(self):
        '''This function returns the top 10 most occuring words'''
        valid_data = self.validated_data
        lines_temp = re.split('\W+', str(valid_data["text"])) #Tokenising

        filtered_sentence = []
        for word in lines_temp:
            if word not in stop_words: #Removing stop words
                filtered_sentence.append(word)

        '''Finding top 10 most occuring words'''
        most_occur = Counter(filtered_sentence).most_common(10)

        return most_occur


    def most_imp(self):
        '''This function returns the top 10 most important words'''
        valid_data = self.validated_data

        lines_temp = re.split('\W+', str(valid_data["text"])) #Tokenising

        filtered_sentence = []
        for word in lines_temp:
            if word not in stop_words: #Removing stop words
                filtered_sentence.append(word)

        count = Convert(Counter(filtered_sentence).most_common())
        tf = computeTF(count,filtered_sentence)
        tfidf = computeTFIDF(tf, idfs)
        sorted_d = dict(sorted(tfidf.items(), key=operator.itemgetter(1),reverse=True))
        most_important = dict(itertools.islice(sorted_d.items(), 10))

        return most_important
