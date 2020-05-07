from rest_framework import serializers
from livros.models import Livro, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class LivrosSerializer(serializers.ModelSerializer):
    #disponivel = serializers.ReadOnlyField()
    categoria = CategoriaSerializer()

    class Meta:
        model = Livro
        fields = ['nome', 'categoria', 'autor']


