from django.contrib import admin
from  livros.models import Livro, Categoria

# Register your models here.
admin.site.register([Livro, Categoria])