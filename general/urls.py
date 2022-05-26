from django.urls import path, include
from .views import (
    SocialMediaApiView,
    AboutMeApiView,
    ContactMeApiView,
    MessageApiView,
    TitlesApiView
)


urlpatterns = [
    path('social/', SocialMediaApiView.as_view()),
    path('about/', AboutMeApiView.as_view()),
    path('contact/', ContactMeApiView.as_view()),
    path('message/', MessageApiView.as_view()),
    path('titles/', TitlesApiView.as_view()),

]