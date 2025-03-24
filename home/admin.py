from django.contrib import admin

from .models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'titulo_topico_um', 'topico_um')
