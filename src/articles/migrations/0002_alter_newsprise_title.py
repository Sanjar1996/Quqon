# Generated by Django 3.2.6 on 2021-09-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsprise',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]