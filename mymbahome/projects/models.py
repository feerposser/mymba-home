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
        db_table = "contributor"


class ModelImageActivity(models.Model):
    image = models.ImageField(upload_to="activity", verbose_name="Imagem", default="", null=True, blank=True,
                              help_text="'x'px 'x'px")

    def __str__(self):
        return self.image.name

    class Meta:
        db_table = "activity_image"


class ModelLink(models.Model):
    link = models.URLField()

    def __str__(self):
        return self.link.name

    class Meta:
        db_table = "activity_link"


class ModelTypeActivity(models.Model):
    type_activity = (
        ("project", "Projeto"),
        ("action", "Ação"),
        ("deleted", "Deletado")
    )

    type = models.CharField(max_length=20, null=False, blank=False, choices=type_activity,
                            unique=True,
                            verbose_name="Tipo de atividade",
                            help_text="Ação: atividade pontual ou recorrente\nProjeto: atividade constante")

    def __str__(self):
        return self.type

    @staticmethod
    def get_or_create_default():
        return ModelTypeActivity.objects.get_or_create(type="deleted")

    def get_verbose_type(self):
        """
        Select the verbose type activity instanced.
        :return: str verbose from choice tuple.
        """
        for no_verbose, verbose in self.type_activity:
            if no_verbose == self.type:
                return verbose

    class Meta:
        db_table = "activity_type"


class ModelActivity(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    slug_name = models.SlugField(max_length=100, verbose_name="URL do conteúdo")
    type = models.ForeignKey(ModelTypeActivity,
                             on_delete=models.SET(ModelTypeActivity.get_or_create_default),
                             default=ModelTypeActivity.get_or_create_default)
    headline = models.TextField(max_length=250, help_text="250 caracteres", verbose_name="Resumo")
    description = models.TextField(verbose_name="Descrição")
    impacted_animals = models.IntegerField(blank=True, null=True, verbose_name="Animais impactados",
                                           help_text="Número inteiro")
    images = models.ManyToManyField(ModelImageActivity, blank=False, verbose_name="Imagens")
    contributors = models.ManyToManyField(ModelContributor, blank=True, verbose_name="Contribuintes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"
        db_table = "activity"
