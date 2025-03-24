from django.shortcuts import render

from .models import Home
from datetime import datetime

def home(request):
    #recupera o conteudo da pagina home
    home = Home.objects.filter().first()

    return render(request, 'home/home.html',{'home' : home, 'footer_text':home.rodape, 'footer_year':datetime.now().year})