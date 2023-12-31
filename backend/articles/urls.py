"""url routes app."""

from django.urls import path
from . import views


urlpatterns = [
    path("articles", views.new_article),
    # path("add/", views.register),
    # path("file/", views.translate_file),
    # path("image/", views.translate_image),
    # path("texte/", views.translate_texte),
]
