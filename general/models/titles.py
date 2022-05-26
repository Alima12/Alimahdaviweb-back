from utils.general_model import GeneralModel
from django.db import models
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f"titles/{instance.pk}/", filename)


class Titles(GeneralModel):
    web_title = models.CharField(
        max_length=50
    )
    browser_title = models.CharField(
        max_length=70
    )
    background = models.ImageField(
        upload_to=get_file_path,
        null= True
    )
    name = models.CharField(
        max_length=30
    )
    my_skill = models.ManyToManyField("sampleworks.skills", related_name="skills")
    short_description = models.TextField()