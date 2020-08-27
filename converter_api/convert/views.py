from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serialisers import ConvertFileSerialiser
from rest_framework.parsers import MultiPartParser

class PdftoText(APIView):

    parser_classes = [MultiPartParser]

    def post():
        serialiser = ConvertFileSerialiser(data = request.data)

        if serialiser.is_valid():
            ret = dict()
            ret['text'] = serialiser.conv()
            return Response(ret, status.HTTP_200_OK)

        data = serializer.errors
        return Response(data, status.HTTP_400_BAD_REQUEST)
