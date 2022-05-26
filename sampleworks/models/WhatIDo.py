from django.db import models
from utils.general_model import GeneralModel


class IDo(GeneralModel):
    title = models.CharField(
        max_length=20
    )
    short_description = models.TextField()
    icon = models.CharField(
        max_length=30,
        null=True
    )
