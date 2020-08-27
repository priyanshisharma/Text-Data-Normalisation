from rest_framework import serializers
import re
from collections import Counter
import string 
import operator
import itertools
from .converter import stop_words, idfs, Convert,computeTF, computeTFIDF

class ConvertFileSerialiser(serializers.Serializer):
    pdf_file = serializers.FileField()

    def conv(self):
        try:
            pdf = pdftotext.PDF(pdf_file)
        except:
            raise serializers.ValidationError({"file_type":"Please enter file with '.pdf' extension"})

        pdf_lines = str()
        for page in pdf:
            pdf_lines += str(page)

        return pdf_file


class ConvertTextSerialiser(serializers.Serializer):
    text = serializers.CharField()

    def most_occ(self):
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
        valid_data = self.validated_data

        lines_temp = re.split('\W+', str(valid_data["text"])) #Tokenising

        filtered_sentence = []
        for word in lines_temp:
            if word not in stop_words: #Removing stop words
                filtered_sentence.append(word)

        count = Convert(Counter(filtered_sentence).most_common())
        tf = computeTF(count,filtered_sentence)
        tfidf =  computeTFIDF(tf,idfs)
        sorted_d = dict(sorted(tfidf.items(), key=operator.itemgetter(1),reverse=True))
        most_important = dict(itertools.islice(sorted_d.items(), 10))

        return most_important
    

