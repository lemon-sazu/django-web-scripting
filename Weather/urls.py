from .views import index
from django.urls import path

urlpatterns = [
    path('news', index, name='news'),
]
