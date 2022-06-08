from django.urls import path, include
from .views import (
    receive_messages
)


urlpatterns = [
    path('receive/', receive_messages),

]