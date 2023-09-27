from django.urls import path, include	# include is used to include other urls.py files
from .views import index, cliente, soporte, recepcion, administracion

urlpatterns = [
	path('', index, name='index'),
	path('cliente/', cliente, name='cliente'),
	path('soporte/', soporte, name='soporte'),
	path('recepcion/', recepcion, name='recepcion'),
	path('administracion/', administracion, name='administracion'),
]
