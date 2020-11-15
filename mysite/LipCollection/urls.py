from . import views
from django.urls import path

app_name = 'LipCollection'

urlpatterns = [
    path('', views.about, name="about"),
]