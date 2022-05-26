from rest_framework import serializers
from general.models.social_media import SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"