from rest_framework import serializers
from sampleworks.models import Sample, Skills, IDo


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = "__all__"


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class WhatIDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDo
        fields = "__all__"