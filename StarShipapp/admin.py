from django.contrib import admin
from StarShipapp.models import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Nave)
admin.site.register(Corveta_Nave)
admin.site.register(StarFight_Nave)
admin.site.register(Cargo_Nave)

