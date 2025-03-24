#BaseCommand: classe base para criar comandos personalizados no Django. Ao herdar essa classe, pode ser criado
#comandos que são executados pelo manage.py no terminal.

from django.core.management.base import BaseCommand

#Home: Importar o modelo Home da aplicação home. O modelo represnta a tabela no banco de dados onde os dados serão
# manipulados.

from home.models import Home

class Command(BaseCommand):

    ajuda = 'Seed para cadastrar registro na tabela Home'

    def handle(self, *args, **kwargs):
        home = {
            'titulo': 'Site para auxílio e direcionamento no desempenho academico de estudantes',
            'subtitulo': 'Subtítulo do site',
            'titulo_topico_um': 'Titulo do primeiro tópico',
            'topico_um': 'Texto do primeiro tópico',
            'titulo_topico_dois': 'Titulo do segundo tópico',
            'topico_dois': 'Texto do segundo tópico',
            'titulo_topico_tres':'Titulo do terceiro tópico',
            'topico_tres':'Texto do terceiro tópico',
            'rodape':'Texto do rodape'
        }

        #Atualiza o registro existente ou cria um novo com base no titulo
        Home.objects.update_or_create(
            titulo=home['titulo'], #criterio de busca: titulo
            defaults=home #valores padrao para criar ou atualizar
        )

        #Comando para exibir uma mensagem no terminal indicando que as alteracoes deram certo
        self.stdout.write(self.style.SUCCESS('Conteudo da pagina inicial adicionado com sucesso.'))