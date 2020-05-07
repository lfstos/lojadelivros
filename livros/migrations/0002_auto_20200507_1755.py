# Generated by Django 3.0.6 on 2020-05-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categotia', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.AddField(
            model_name='livro',
            name='em_estoque',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
