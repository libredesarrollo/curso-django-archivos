from django.urls import path
from . import views

urlpatterns = [
    path('generate_pdf', views.generate_pdf),
    path('generate_pdf2', views.generate_pdf2),
    path('generate_pdf_download', views.generate_pdf_download),
    path('download_file', views.download_file)
]