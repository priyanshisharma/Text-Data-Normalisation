from django.urls import path
from .views import PdftoText, TexttoMostCommon


urlpatterns = [
    path('pdf_to_text/', PdftoText.as_view(), name='convert_pdf_to_text'),
    path('text_to_info/', TexttoMostCommon.as_view(), name='get_info_from_text')
]
