from django.conf.urls import url
from influence import views

# TEMPLATE URLs
app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$', views.user_login, name = 'user_login'),

    path('', views.index, name = 'influencer_profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
