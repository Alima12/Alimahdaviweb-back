from django.db import models
from utils.general_model import GeneralModel


class Skills(GeneralModel):
    name = models.CharField(
        max_length=30
    )
    percent = models.IntegerField()
