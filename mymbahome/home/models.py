import os
from django.core.validators import ValidationError
from django.db import models


def validador_image_size(image):
    file_size = image.file.size
    limit_mb = 1

    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("A imagem possui %s mb. O tamanho máximo de ve ser de %s mb." % (file_size, limit_mb))


class ModelTestimony(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50, blank=True)
    testimony = models.CharField(max_length=200)
    social_media_link = models.URLField(max_length=50)
    image = models.ImageField(upload_to=os.path.join("home", "testimonials"),
                              blank=True,
                              validators=[validador_image_size]
                              )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"
