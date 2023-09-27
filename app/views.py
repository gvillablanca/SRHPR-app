from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def index(request):
		# se verifica que permisos tiene el usuario
		is_cliente = request.user.has_perm('auth.rol_cliente')
		is_recepcion = request.user.has_perm('auth.rol_recepcion')
		is_soporte = request.user.has_perm('auth.rol_soporteti')
		is_admin = request.user.has_perm('auth.rol_admin')

		# se redirecciona a la vista correspondiente aplicando perfilamiento.
		if is_cliente:
			return redirect(to="cliente")
		elif is_recepcion:
			return redirect(to="recepcion")
		elif is_soporte:
			return redirect(to="soporte")
		elif is_admin:
			return redirect(to="administracion")
		else:
			return render(request, 'app/index.html')

def cliente(request):
		is_cliente = request.user.has_perm('auth.rol_cliente')
		is_superuser = request.user.is_superuser
		is_admin = request.user.has_perm('auth.rol_admin')
		if not is_cliente and not is_superuser and not is_admin:
			return redirect(to="index")
		return render(request, 'app/cliente/main.html')

def soporte(request):
		is_soporte = request.user.has_perm('auth.rol_soporteti')
		is_superuser = request.user.is_superuser
		is_admin = request.user.has_perm('auth.rol_admin')
		if not is_soporte and not is_superuser and not is_admin:
			return redirect(to="index")
		return render(request, 'app/soporte/main.html')

def recepcion(request):
		is_recepcion = request.user.has_perm('auth.rol_recepcion')
		is_superuser = request.user.is_superuser
		is_admin = request.user.has_perm('auth.rol_admin')
		if not is_recepcion and not is_superuser and not is_admin:
			return redirect(to="index")
		return render(request, 'app/recepcion/main.html')

def administracion(request):
		is_admin = request.user.has_perm('auth.rol_admin')
		is_superuser = request.user.is_superuser
		if (not is_admin and not is_superuser):
			return redirect(to="index")
		return render(request, 'app/administracion/main.html')
