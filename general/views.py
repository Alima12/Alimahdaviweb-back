from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .serializers import (
    SocialMediaSerializer,
    AboutMeSerializer,
    ContactMeSerializer,
    MessageSerializer,
    TitlesSerializer
)
from .models import (
    SocialMedia,
    AboutMe,
    ContactMe,
    Message,
    Titles
)
from rest_framework.permissions import AllowAny


class SocialMediaApiView(ListCreateAPIView):
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()


class AboutMeApiView(ListCreateAPIView):
    serializer_class = AboutMeSerializer
    queryset = AboutMe.objects.all()


class ContactMeApiView(ListCreateAPIView):
    serializer_class = ContactMeSerializer
    queryset = ContactMe.objects.all()


class MessageApiView(CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = (AllowAny, )


class TitlesApiView(ListCreateAPIView):
    serializer_class = TitlesSerializer
    queryset = Titles.objects.all()