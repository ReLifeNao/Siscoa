from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from Sistema import views
class TestUrls(SimpleTestCase):

    

    def test_Login_url_is_resolved(self):
        url = reverse('Login')
        self.assertEquals(resolve(url).func,views.Login)

    def test_LoginUsuario_url_is_resolved(self):
        url = reverse('LoginUsuario')
        self.assertEquals(resolve(url).func,views.LoginUsuario)


    def test_DocenteCursos_url_is_resolved(self):
        url = reverse('DocenteCursos')
        self.assertEquals(resolve(url).func,views.DocenteCursos)

    def test_SalonMateria_is_resolved(self):
        url = reverse('SalonMateria',args=[1])
        self.assertEquals(resolve(url).func,views.SalonMateria)

    def test_NotaCurso_is_resolved(self):
        url = reverse('NotaCurso',args=[1])
        self.assertEquals(resolve(url).func,views.NotaCurso)

    def test_Logout_is_resolved(self):
        url = reverse('Logout')
        self.assertEquals(resolve(url).func,views.logoutUser)

    def test_Estudiante_url_is_resolved(self):
        url = reverse('Estudiante')
        self.assertEquals(resolve(url).func,views.EstudianteView)
    