from django.urls import path
from . import views
from .views import notse
from .views import ask_question
from .views import chatbot_api

urlpatterns = [
    path('ask-question/', ask_question, name='ask-question'),
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
    path('pricing/index.html', views.notse_index, name='pricing_index'),
    path('notse/pricing.html', views.notse_pricing, name='notse_pricing'),
    path('notse/blog.html', views.notse_blog, name='notse_blog'),
    path('pricing/notse.html', views.pricing_notse, name='pricing_notse'),
    path('pricing/contact.html', views.notse_index, name='pricing_contact'),
    path('pricing/pricing.html', views.pricing, name='pricing_pricing'),
    path('chatbot-api/', chatbot_api, name='chatbot_api'),
    path('api/chatbot-api/', views.chatbot_api, name='chatbot_api'),
    


]

