from django.urls import path
from . import views

urlpatterns = [
    path('csv_read', views.csv_read),
    path('csv_write', views.csv_write),
    path('csv_read_dict', views.csv_read_dict),
    path('csv_write_dict', views.csv_write_dict),
]