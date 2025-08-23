from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.BirthdayTemplateView.as_view(), name='homepage'),
]
