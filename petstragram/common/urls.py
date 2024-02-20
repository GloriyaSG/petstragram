from django.urls import path, include

from petstragram.common.views import index

urlpatterns = (
    path('', index, name='index'),
)