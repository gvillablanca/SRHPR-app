from django.urls import path, include	# include is used to include other urls.py files
from .views import index

urlpatterns = [
  path('', index, name='index'),
]
