from utils.general_model import GeneralModel
from django.db import models
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f"social_media/{instance.pk}/", filename)


class SocialMedia(GeneralModel):
    icon = models.CharField(
        max_length=50
    )
    url = models.URLField()