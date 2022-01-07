from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('the_dungeon', views.the_dungeon, name='the_dungeon'),
    path('the_beach', views.the_beach, name='the_beach'),
    path('the_mayor_of_springfield', views.the_mayor_of_springfield, name='the_mayor_of_springfield'),
    path('the_gordon', views.the_gordon, name='the_gordon'),
    path('about_me', views.about_me, name='about_me'),
]

