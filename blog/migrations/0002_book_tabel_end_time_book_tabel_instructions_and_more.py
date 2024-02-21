# Generated by Django 4.2.9 on 2024-02-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_tabel',
            name='end_time',
            field=models.CharField(default='', max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_tabel',
            name='instructions',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_tabel',
            name='start_time',
            field=models.CharField(default='', max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book_tabel',
            name='Number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_tabel',
            name='Person',
            field=models.IntegerField(),
        ),
    ]
