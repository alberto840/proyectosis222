from django.contrib import admin

from .models import paciente
from .models import personal
from .models import hijo
from .models import encuesta
from .models import idioma
from .models import condicion_medica
from .models import referencia_contacto
# Register your models here.

admin.site.register(paciente)
admin.site.register(personal)
admin.site.register(hijo)
admin.site.register(encuesta)
admin.site.register(idioma)
admin.site.register(condicion_medica)
admin.site.register(referencia_contacto)
