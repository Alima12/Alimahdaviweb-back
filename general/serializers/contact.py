from rest_framework import serializers
from general.models import ContactMe


class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMe
        fields = "__all__"