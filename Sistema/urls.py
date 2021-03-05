from django.urls import path
from . import views
app_name = 'Sistema'

urlpatterns = [

    path('Notas/',views.NotasView,name='NotasView'),
    path('Estudiante/',views.EstudianteView,name='Estudiante'),
    path('Administrador/',views.AdministradorView,name='AdministradorView'),
    path('EstudianteNotas/',views.EstudiantesNotas,name='EstudiantesNotas'),
    path('DocenteCursos/',views.DocenteCursos,name='DocenteCursos'),
    path('Edit/<int:id>/<int:idM>/<int:idS>',views.Edit,name='Edit'),
    path('SalonMateria/<id>/',views.SalonMateria,name='SalonMateria'),
    path('adminhtml',views.adminhtml,name='adminhtml'),
    path('EstudianteNotas/',views.EstudiantesNotas,name='EstudiantesNotas'),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register,name='Register'),
    path('Logout/',views.logoutUser,name='LogoutUser'),


    path('LoginUsuario/',views.LoginUsuario,name='LoginUsuario'),
    path('RegisterUsuario/',views.RegisterUsuario,name='RegisterUsuario'),
    path('LogoutUsuario/',views.logoutUsuario,name='LogoutUsuario'),
    path('NotaCurso/<int:curso>/',views.NotaCurso,name='NotaCurso'),
    path('MostrarAlumnosSinSalon/',views.MostrarAlumnosSinSalon,name='MostrarAlumnosSinSalon'),
    path('AsignarSalon/<int:Alumno>',views.AsignarSalon,name='AsignarSalon'),
    path('MostrarTablaDocente/',views.MostrarTablaDocentes,name='MostrarTablaDocente'),
    path('MostrarTablaEstudiante/',views.MostrarTablaEstudiantes,name='MostrarTablaEstudiante'),


]