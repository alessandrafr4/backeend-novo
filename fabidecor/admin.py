from django.contrib import admin

from .models import Categoria, Produto, Tema
from fabidecor.models import Compra

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Tema)
admin.site.register(Compra)



