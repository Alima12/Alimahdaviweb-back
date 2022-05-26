from django.db import models
from utils.general_model import GeneralModel
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f"product/{instance.pk}/", filename)


class Sample(GeneralModel):
    title = models.CharField(
        max_length=20
    )
    thumb_nail = models.ImageField(
        upload_to=get_file_path
    )
    description = models.TextField()
    owner = models.CharField(
        max_length=50
    )
    url = models.CharField(
        max_length=100
    )