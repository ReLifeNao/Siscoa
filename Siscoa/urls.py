"""Siscoa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Notas/',views.NotasView),
    path('Estudiante/',views.EstudianteView,name='Estudiante'),
    path('Administrador/',views.AdministradorView),
    path('EstudianteNotas/',views.EstudiantesNotas),
    path('DocenteCursos/',views.DocenteCursos,name='DocenteCursos'),
    path('Edit/<int:id>/<int:idM>/<int:idS>',views.Edit),
    path('SalonMateria/<id>/',views.SalonMateria,name='SalonMateria'),

    path('EstudianteNotas/',views.EstudiantesNotas),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register),
    path('Logout/',views.logoutUser,name='Logout'),


    path('LoginUsuario/',views.LoginUsuario,name='LoginUsuario'),
    path('RegisterUsuario/',views.RegisterUsuario),
    path('LogoutUsuario/',views.logoutUsuario),
    path('NotaCurso/<int:curso>/',views.NotaCurso,name='NotaCurso'),
    path('MostrarAlumnosSinSalon/',views.MostrarAlumnosSinSalon),
    path('AsignarSalon/<int:Alumno>',views.AsignarSalon),


]
