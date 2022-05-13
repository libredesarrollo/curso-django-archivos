from django.urls import path
from . import views

urlpatterns = [
    path('excel_writer', views.excel_writer),
    path('excel_read', views.excel_read)
]