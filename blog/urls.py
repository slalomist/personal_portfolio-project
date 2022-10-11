from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.all_blocks, name="all_blocks"),
    path("<int:blog_id>/", views.detail, name="detail")
]
