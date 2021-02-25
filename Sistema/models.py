from django.db import models

class Salon(models.Model):
    Id_Salon = models.CharField(max_length=50)
    Grado = models.CharField(max_length=3)
    Seccion = models.CharField(max_length=10)
    

   

class TipoUsuario(models.Model):
    Id_TipoUsuario = models.CharField(primary_key=True,max_length=50)
    
    Descripcion = models.CharField(max_length=100)

class Docente(models.Model):
    Id_Docente = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    User = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    


    

class Materia(models.Model):
    Id_Materia = models.CharField(primary_key=True,max_length=50)
    
    Nombre_Curso = models.CharField(max_length=40)
    Id_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    Id_Salon = models.ForeignKey(Salon, on_delete=models.CASCADE)


class Apoderado(models.Model):
    Id_Apoderado = models.CharField(primary_key=True,max_length=50)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Celular = models.IntegerField()
    Correo = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)



class Administrador(models.Model):
    Id_Administrador = models.CharField(primary_key=True,max_length=50)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Celular = models.IntegerField()
    Correo = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

class Director(models.Model):
    Id_Director = models.CharField(primary_key=True,max_length=50)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Celular = models.IntegerField()
    Correo = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)



class Estudiante(models.Model):
    Id_Estudiante = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    User = models.CharField(max_length=50)
    Correo = models.CharField(max_length=50)
    Tipo_Usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    Salon = models.ForeignKey(Salon, on_delete=models.CASCADE,null=True)

class Vinculo_Familiar(models.Model):
    Id_VinculoFamiliar = models.CharField(primary_key=True,max_length=50)
    Id_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Id_Apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    Descripcion = models.CharField(max_length=100)

class Bimestre(models.Model):
    Id_Bimestre = models.CharField(primary_key=True,max_length=50)
    Bimestre1 = models.IntegerField()
    Bimestre2 = models.IntegerField()
    Bimestre3 = models.IntegerField()
    Bimestre4 = models.IntegerField()

#class Detalle_Asistencia(models.Model):
    #Id_Detalle = models.CharField(primary_key=True,max_length=50)
    #Asistio = models.CharField(max_length=10)
    #Tardanza = models.CharField(max_length=10)
    #Falta = models.CharField(max_length=10)
    #Falta_Justificada = models.CharField(max_length=10)
    #Tardanza_Justificada = models.CharField(max_length=10)
    #Fecha = models.DateField()

#class Asistencias(models.Model):
    #Id_Asistencia = models.CharField(primary_key=True,max_length=50)
    #Id_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    #Id_Bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE)
    #Id_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    #Id_Detalle = models.ForeignKey(Detalle_Asistencia, on_delete=models.CASCADE)

class Notas(models.Model):
    Id_Notas = models.CharField(primary_key=True,max_length=50)
    Id_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Id_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Id_Bimestre = models.OneToOneField(Bimestre,on_delete=models.CASCADE)
    #
    Fecha = models.DateField()
    Id_SalonC = models.ForeignKey(Salon, on_delete=models.CASCADE)
    HoraRegistro = models.DateTimeField(null=True)

class Reporte_Notas(models.Model):
    Id_ReporteNotas = models.CharField(primary_key=True,max_length=50)
    Id_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Id_Salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    Id_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    Id_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Id_Bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE)

#class Reporte_Asistencia(models.Model):
    #Id_ReporteAsistencia = models.CharField(primary_key=True,max_length=50)
    #Id_Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    #Id_Asistencia = models.ForeignKey(Asistencias, on_delete=models.CASCADE)
    #Id_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    #Id_Bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE)





