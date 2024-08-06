from django.urls import path
from . import views
from .views import notse

urlpatterns = [
    path('', views.index, name='index'),
    path('notse/', views.notse, name='notse'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('reset_password/', views.login, name='reset_password'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signup_action/', views.signup_action, name='signup_action'),
    path('profile/', views.profile, name='profile'),
    path('notse/index.html', views.notse_index, name='notse_index'),
    


]
