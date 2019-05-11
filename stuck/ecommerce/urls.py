from django.conf.urls import url
from ecommerce import views


app_name = 'ecommerce'


urlpatterns = [
    url('', views.index, name='index'),
]
