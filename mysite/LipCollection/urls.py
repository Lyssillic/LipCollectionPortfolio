from . import views
from django.urls import path

app_name = 'LipCollection'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('balm/', views.balm, name="balm"),
    path('gloss/', views.gloss, name="gloss"),
    path('scrub/', views.scrub, name="scrub"),
    path('<int:id>', views.detail, name="detail"),
]
