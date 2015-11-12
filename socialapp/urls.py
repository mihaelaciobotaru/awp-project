from django.conf.urls import url

from socialapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
