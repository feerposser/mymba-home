from django.db import models


class ModelContributor(models.Model):
    name = models.CharField(max_length=100)
    social_media_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contribuinte"
        verbose_name_plural = "Contribuintes"
        ordering = ["name"]


class ModelImageActivity(models.Model):
    image = models.ImageField(upload_to="activity", verbose_name="Imagem", default="", null=True, blank=True,
                              help_text="'x'px 'x'px")


class ModelLink(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link.name


class ModelActivity(models.Model):

    type_activity = (
        ("Projeto", "Projeto"),
        ("Ação", "Ação"),
    )

    name = models.CharField(max_length=50, verbose_name="Nome")
    type = models.CharField(max_length=20, null=False, blank=False, choices=type_activity,
                            verbose_name="Tipo de atividade",
                            help_text="Ação: atividade pontual ou recorrente\nProjeto: atividade constante")
    headline = models.TextField(max_length=250, help_text="250 caracteres", verbose_name="Resumo")
    description = models.TextField(verbose_name="Descrição")
    impacted_animals = models.IntegerField(blank=True, null=True, verbose_name="Animais impactados",
                                           help_text="Número inteiro")
    images = models.ManyToManyField(ModelImageActivity, blank=False, verbose_name="Imagens")
    contributors = models.ManyToManyField(ModelContributor, blank=True, verbose_name="Contribuintes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        db_table = "activity"
