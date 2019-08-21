from django.urls import path
from . import views
# from django.views.generic import TemplateView

app_name = 'api'
urlpatterns = [
    path('message', views.message, name='message'),
]