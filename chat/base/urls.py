from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>', views.room, name='room'),

    path('create_room', views.create_room, name="create_room"),
    path('update_room/<str:pk>', views.update_room, name="update_room"),
    path('delete_room/<str:pk>', views.delete_room, name="delete_room"),

    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_user, name="logout"),  
]


