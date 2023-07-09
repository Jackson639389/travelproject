from . import views
from django.urls import path

app_name = 'gaming'


urlpatterns = [
    path('',views.web,name='website'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

]