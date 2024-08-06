from django.urls import path
from . import views
from .views import notse_view, contact_view

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # URL pattern for index.html
    path('contact/', views.contact, name='contact'), 
    path('blog/', views.blog, name='blog'),
    path('notse/', views.notse, name='notse'),
    path('notse/', notse_view, name='notse'), 
]
