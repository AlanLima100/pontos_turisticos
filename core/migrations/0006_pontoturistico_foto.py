# Generated by Django 3.2.22 on 2023-11-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_pontoturistico_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(null=True, upload_to='pontos_turisticos'),
        ),
    ]
