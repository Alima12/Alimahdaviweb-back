from utils.general_model import GeneralModel
from django.db import models


class ContactMe(GeneralModel):
    phone_number = models.CharField(
        max_length=12
    )
    email = models.EmailField()
    address = models.TextField()