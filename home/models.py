from django.db import models

class Home(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    subtitulo = models.CharField(max_length=255, verbose_name="Subtítulo")
    titulo_topico_um = models.CharField(max_length=50, verbose_name="Título Tópico 1")
    topico_um = models.TextField(verbose_name="Tópico 1")
    titulo_topico_dois = models.CharField(max_length=50, verbose_name="Título Tópico 2")
    topico_dois = models.TextField(verbose_name="Tópico 2")
    titulo_topico_tres = models.CharField(max_length=50, verbose_name="Título Tópico 3")
    topico_tres = models.TextField(verbose_name="Tópico 3")
    rodape = models.TextField(max_length=10, verbose_name="Rodape",default="Texto padrao para rodape")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Página Inicial"
        verbose_name_plural = "Páginas Iniciais"
