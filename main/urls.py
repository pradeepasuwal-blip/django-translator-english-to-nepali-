from django.urls import path
from .views import home,translate_api

urlpatterns = [
    path('', home, name='home'),
    path('api/translate/', translate_api),
]