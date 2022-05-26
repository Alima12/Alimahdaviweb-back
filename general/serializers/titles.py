from rest_framework import serializers
from general.models import Titles


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = "__all__"
        depth = 1