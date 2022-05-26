from rest_framework.generics import ListCreateAPIView
from .serializer import SampleSerializer, SkillsSerializer, WhatIDoSerializer
from .models import Sample, Skills, IDo


class CreateSampleApi(ListCreateAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()


class SkillsViewApi(ListCreateAPIView):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()


class WhatIDoViewApi(ListCreateAPIView):
    serializer_class = WhatIDoSerializer
    queryset = IDo.objects.all()
