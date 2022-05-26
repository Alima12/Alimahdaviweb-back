from utils.general_model import GeneralModel
from django.db import models


class Message(GeneralModel):
    name = models.CharField(
        max_length=50
    )
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name}- {self.message[0:30]}"