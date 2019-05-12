from django.urls import path
from ecommerce import views


app_name = 'ecommerce'


urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.see_influencer, name='see'),
    path('getuser/', views.get_user, name = 'get_user'),
    path('email/', views.email, name = 'email')
]
