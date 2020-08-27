from rest_framework import serializers

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

    