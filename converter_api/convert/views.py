from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .serialisers import ConvertFileSerialiser, ConvertTextSerialiser

class PdftoText(APIView):

    parser_classes = [MultiPartParser]

    def post(self, request):
        serialiser = ConvertFileSerialiser(data = request.data)

        if serialiser.is_valid():
            ret = dict()
            ret['text'] = serialiser.conv()
            return Response(ret, status.HTTP_200_OK)

        data = serialiser.errors
        return Response(data, status.HTTP_400_BAD_REQUEST)


class TexttoMostCommon(APIView):

    def post(self, request):
        serialiser = ConvertTextSerialiser(data = request.data)

        if serialiser.is_valid():
            ret = dict()
            ret['most frequent words'] = serialiser.most_occ()
            ret['most important words'] = serialiser.most_imp()
            return Response(ret, status.HTTP_200_OK)

        data = serialiser.errors
        return Response(data, status.HTTP_400_BAD_REQUEST)
