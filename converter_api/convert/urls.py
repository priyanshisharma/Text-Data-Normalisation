from django.urls import path
from .views import PdftoText


urlpatterns = [	
    path('pt/', PdftoText.as_view(), name='convert_pdf_to_text'),
]