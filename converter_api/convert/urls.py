from django.urls import path
from .views import PdftoText, TexttoMostCommon


urlpatterns = [	
    path('pt/', PdftoText.as_view(), name='convert_pdf_to_text'),
    path('tc/', TexttoMostCommon.as_view(), name='text_to_info')
]