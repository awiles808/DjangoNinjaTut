# Generated by Django 2.0.5 on 2018-05-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
