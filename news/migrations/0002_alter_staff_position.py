# Generated by Django 4.1.3 on 2022-11-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('DI', 'Директор'), ('AD', 'Администратор'), ('CO', 'Повар'), ('CA', 'Кассир'), ('CL', 'Уборщик')], default='CA', max_length=2),
        ),
    ]
