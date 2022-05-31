from django.db import models

# Create your models here.

class Paciente(models.Model):
    paciente_id = models.PositiveIntegerField()

    # Atributos heredados originalmente de la clase persona
    ci = models.PositiveIntegerField()
    nombre_completo = models.CharField(max_length=100)
    fechanac=models.DateField()
    celular = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)

    # Atributos unicos de paciente
    profesion = models.CharField(max_length=30)
    estado_civil = models.CharField(max_length=30)
    grado_instruccion = models.CharField(max_length=30)
    estado_salud = models.CharField(max_length=30)
    observaciones = models.CharField(max_length=1000)
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=100)
    puntaje_minimental = models.PositiveIntegerField()
    medicacion = models.CharField(max_length=100)
    lugarnac = models.CharField(max_length=50)
    
    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_completo, self.ci,self.celular)

class Hijo(models.Model):
    hijo_id = models.PositiveIntegerField()
    # Atributos heredados originalmente de la clase persona
    
    ci = models.PositiveIntegerField()
    nombre_completo = models.CharField(max_length=100)
    fechanac=models.DateField()
    celular = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_completo, self.ci,self.celular)

class Encuesta(models.Model):
    gds_id = models.PositiveIntegerField()
    nombre_prueba = models.CharField(max_length=100)
    pregunta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=200)
    fecha = models.DateField()
    tipo = models.CharField(max_length=30)

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.gds_id, self.nombre_prueba)

class Idioma(models.Model):
    idioma_id = models.PositiveIntegerField()
    idioma = models.CharField(max_length=30)
    nativo = models.BooleanField()

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.idioma_id, self.idioma)

class Condicion_medica(models.Model):
    condicion_medica_id = models.PositiveIntegerField()
    enfermedad = models.CharField(max_length=300)
    medicacion = models.CharField(max_length=30)
    nativo = models.BooleanField()
    fecha_inicio = models.DateField()

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.condicion_medica_id, self.enfermedad)

class Referencia_contacto(models.Model):
    referencia_contacto_id = models.PositiveIntegerField()    
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.PositiveIntegerField()
    
    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_contacto,self.telefono_contacto)










