from django.db import router
from .views import RequesForms, GetData
from rest_framework import routers, urlpatterns, views
from django.urls import path, include
# router = routers.DefaultRouter()
# router.register('persona', RequesForms)

urlpatterns = [
    path('', RequesForms.as_view(), name='page'),
    path('data/', GetData.as_view(), name='api sharsprin')
]