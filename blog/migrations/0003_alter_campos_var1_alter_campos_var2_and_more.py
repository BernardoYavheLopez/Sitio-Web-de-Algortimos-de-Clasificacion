# Generated by Django 4.1.1 on 2022-09-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_campo_campos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campos',
            name='var1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campos',
            name='var2',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='campos',
            name='var3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campos',
            name='var4',
            field=models.FloatField(blank=True, null=True),
        ),
    ]