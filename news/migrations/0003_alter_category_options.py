# Generated by Django 4.2.13 on 2024-05-23 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
