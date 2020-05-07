from rest_framework import viewsets
from livros.models import Livro
from livros.serializer import LivrosSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all().select_related('categoria')
    serializer_class = LivrosSerializer