from django.db import router
from .views import RequesForms, hola
from rest_framework import routers, urlpatterns, views
from django.urls import path, include
from .views import hola
# router = routers.DefaultRouter()
# router.register('persona', RequesForms)

urlpatterns = [
    path('', hola),
    path('api/', RequesForms.as_view()),
]