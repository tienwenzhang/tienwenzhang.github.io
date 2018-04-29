from django.urls import path

from . import views

urlpatterns = [
    path('/index', views.index, name = 'index'),
    path('/contact', views.contact, name = 'contact'),
    path('/blog', views.blog, name = 'blog'),
    path('/portfolio', views.portfolio, name = 'portfolio'),
    path('/services', views.services, name = 'services')
]
