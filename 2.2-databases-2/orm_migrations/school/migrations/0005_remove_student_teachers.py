# Generated by Django 4.1.7 on 2023-03-20 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_studentteacher_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
    ]
