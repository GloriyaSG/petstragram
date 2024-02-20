from django.urls import path, include

from petstragram.photos.views import create_photo, details_photo, edit_photo

urlpatterns = (
    path('add/', create_photo, name='add photo'),
    path(
        "<int:pk>/", include([
            path("", details_photo, name='details photo'),
            path('edit/', edit_photo, name='edit photo')
        ]),
    ),
)
