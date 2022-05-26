from utils.general_model import GeneralModel
from django.db import models


class AboutMe(GeneralModel):
    title = models.CharField(
        max_length=50
    )
    short_description = models.CharField(
        max_length=100
    )
    text = models.TextField()