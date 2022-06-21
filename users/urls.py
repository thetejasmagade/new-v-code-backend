from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetails.as_view()),
    path('users/demo/', views.demoPost, name='demo')
]
