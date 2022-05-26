from django.urls import path
from .views import CreateSampleApi, WhatIDoViewApi, SkillsViewApi


urlpatterns = [
    path('', CreateSampleApi.as_view()),
    path('skills/', SkillsViewApi.as_view()),
    path('ido/', WhatIDoViewApi.as_view()),

]