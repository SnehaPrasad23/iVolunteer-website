from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('category/<int:cat>/',views.category, name='category'),
    path('myevents/<int:userid>/',views.myevents, name='myevents'),
    path('registerEvent', views.registerEvent, name='registerEvent'),
    path('unregisterEvent', views.unregisterEvent, name='unregisterEvent')
]