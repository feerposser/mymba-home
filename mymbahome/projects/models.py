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


class ModelProject(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    headline = models.TextField(max_length=250, help_text="250 caracteres", verbose_name="Resumo")
    description = models.TextField(verbose_name="Descrição")
    contributors = models.ManyToManyField(ModelContributor, blank=True, verbose_name="Contribuintes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ["name"]


class ModelAction(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    headline = models.CharField(max_length=250, verbose_name="Resumo", help_text="250 caracteres")
    description = models.TextField(verbose_name="Descricão")
    impacted_animals = models.IntegerField(blank=True, null=True, verbose_name="Animais impactados",
                                           help_text="Número inteiro")
    contributors = models.ManyToManyField(ModelContributor, blank=True, verbose_name="Contribuintes")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ["name"]
