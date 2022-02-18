from django.db import router
from .views import PersonaViewsets, hola
from rest_framework import routers, urlpatterns, views
from django.urls import path, include
from .views import hola
router = routers.DefaultRouter()
router.register('persona', PersonaViewsets)

urlpatterns = [
    path('', hola),
    path('api/', include(router.urls)),
]