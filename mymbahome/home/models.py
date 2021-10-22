import os
from django.core.validators import ValidationError
from django.db import models


def validador_image_size(image):
    file_size = image.file.size
    limit_mb = 1

    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("A imagem possui %s mb. O tamanho máximo de ve ser de %s mb." % (file_size, limit_mb))


class ModelTestimony(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    profession = models.CharField(max_length=50, blank=True, verbose_name="Profissão")
    testimony = models.CharField(max_length=200, verbose_name="Depoimento")
    social_media_link = models.URLField(max_length=50, verbose_name="Link")
    image = models.ImageField(upload_to=os.path.join("home", "testimonials"),
                              blank=True,
                              validators=[validador_image_size],
                              verbose_name="Imagem")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"


class ModelContact(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    office = models.TextField(max_length=50, verbose_name="Ocupação")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"


class ModelFAQ(models.Model):
    question = models.CharField(max_length=200, verbose_name="Pergunta")
    answer = models.TextField(verbose_name="Resposta")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        db_table = "faq"


class ModelNewsletterAssign(models.Model):
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Assinatura de Newsletter"
        verbose_name_plural = "Assinaturas de Newsletter"
        db_table = "newsletter_assign"
