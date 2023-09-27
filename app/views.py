from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def cliente(request):
		return render(request, 'app/cliente/home.html')

def soporte(request):
		return render(request, 'app/soporte/main.html')

def recepcion(request):
		return render(request, 'app/recepcion/main.html')

def administracion(request):
	return render(request, 'app/administracion/main.html')
