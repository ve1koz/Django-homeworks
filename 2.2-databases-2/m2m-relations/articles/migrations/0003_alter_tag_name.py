# Generated by Django 4.1.7 on 2023-03-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_tag_scope_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=60, verbose_name='тэг'),
        ),
    ]