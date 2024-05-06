from django.urls import path
from .views import ExportBookData

urlpatterns = [
    path('', ExportBookData.as_view(), name='book_data')
]
