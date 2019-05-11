from django.urls import path
from influence import views


app_name = 'influence'


urlpatterns = [
    path('', views.index, name = 'index'),
    path('request/', views.update_info, name ='request'),
]
