# Generated by Django 3.1.7 on 2021-07-29 13:31

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_modelnewsletterassign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltestimony',
            name='image',
            field=models.ImageField(blank=True, upload_to='home/testimonials', validators=[home.models.validador_image_size], verbose_name='Imagem'),
        ),
    ]