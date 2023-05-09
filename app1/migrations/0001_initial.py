# Generated by Django 4.2 on 2023-05-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Texte',
            fields=[
                ('key', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Schlüssel')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texte',
            },
        ),
    ]
