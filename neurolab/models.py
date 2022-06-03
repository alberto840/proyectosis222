from django.db import models

# Create your models here.

class paciente(models.Model):
    # Atributos heredados originalmente de la clase persona
    paciente_id = models.CharField(primary_key=True,max_length=6)
    paciente_ci = models.CharField(max_length=10)
    paciente_nombre_completo = models.CharField(max_length=100)
    paciente_fechanac=models.DateField()
    paciente_celular = models.CharField(max_length=10)
    paciente_email = models.EmailField()
    paciente_genero = models.CharField(max_length=30)
    # Atributos unicos de paciente
    profesion = models.CharField(max_length=30)
    estado_civil = models.CharField(max_length=30)
    grado_instruccion = models.CharField(max_length=30)
    estado_salud = models.CharField(max_length=30)
    observaciones = models.CharField(max_length=1000)
    direccion = models.CharField(max_length=100)
    puntaje_minimental = models.PositiveIntegerField()
    medicacion = models.CharField(max_length=100)
    lugarnac = models.CharField(max_length=50)
    
    def __str__(self):
        texto = "{0} - {1} - {2}"
        return texto.format(self.paciente_nombre_completo, self.paciente_ci, self.paciente_celular)


class personal(models.Model):
    # Atributos heredados originalmente de la clase persona
    personal_id=models.CharField(primary_key=True,max_length=6)
    personal_ci = models.CharField(max_length=10)
    personal_nombre_completo = models.CharField(max_length=100)
    personal_fechanac=models.DateField()
    personal_celular =models.CharField(max_length=10)
    personal_email = models.EmailField()
    personal_genero = models.CharField(max_length=30)
    # Atributos unicos de Personal
    especialidad=models.CharField(max_length=50)
    cargo=models.CharField(max_length=50)

    def __str__(self):
        texto1 = "{0} ({1})"
        return texto1.format(self.personal_nombre_completo, self.especialidad)

class hijo(models.Model):
    hijo_id = models.CharField(primary_key=True,max_length=6)
    # Atributos heredados originalmente de la clase persona
    hijo_ci = models.PositiveIntegerField()
    hijo_nombre_completo = models.CharField(max_length=100)
    hijo_fechanac=models.DateField()
    hijo_celular = models.CharField(max_length=10)
    hijo_email = models.EmailField()
    hijo_genero = models.CharField(max_length=30)
    pac=models.ForeignKey(paciente,on_delete=models.CASCADE,
    null=False, blank=False)
    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.hijo_nombre_completo, self.ci,self.hijo_celular)

class encuesta(models.Model):
    gds_id = models.CharField(primary_key=True,max_length=6)
    nombre_prueba = models.CharField(max_length=100)
    pregunta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=200)
    fecha = models.DateField()
    tipo = models.CharField(max_length=30)
    pac=models.ForeignKey(paciente,on_delete=models.CASCADE,
    null=False, blank=False)
    per=models.ForeignKey(personal,on_delete=models.CASCADE,
    null=False, blank=False)

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.gds_id, self.nombre_prueba)

class idioma(models.Model):
    idioma_id = models.CharField(primary_key=True,max_length=6)
    idioma = models.CharField(max_length=30)
    nativo = models.BooleanField()
    pac=models.ForeignKey(paciente,on_delete=models.CASCADE,
    null=False, blank=False)

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.idioma_id, self.idioma)

class condicion_medica(models.Model):
    condicion_medica_id = models.CharField(primary_key=True,max_length=6)
    enfermedad = models.CharField(max_length=300)
    medicacion = models.CharField(max_length=30)
    nativo = models.BooleanField()
    fecha_inicio = models.DateField()
    pac=models.ForeignKey(paciente,on_delete=models.CASCADE,
    null=False, blank=False)

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.condicion_medica_id, self.enfermedad)

class referencia_contacto(models.Model):
    referencia_contacto_id = models.CharField(primary_key=True,max_length=6)    
    nombre_contacto = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=10)
    pac=models.ForeignKey(paciente,on_delete=models.CASCADE,
    null=False, blank=False)

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_contacto,self.telefono_contacto)