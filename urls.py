from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       path('', views.post_list, name='post_list'),
       path('post/<int:id>/',views.post_detail, name='post_detail'),
       path('post/<int:id>/edit/', views.post_edit, name='edit'),
       path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
       path('create-post', views.post_create, name='create'),
       path('admin/', admin.site.urls),
       path('login-page/', views.login_page, name='login'),
       path('register-page/', views.register_page, name='register'),
       path('logout/', views.logout_page, name='logout_view'),
       
   ]
   