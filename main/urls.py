from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('register', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/work', profile_work, name='profile_work'),
    path('profile/new', profile_new, name='profile_new'),
    path('profile/done', profile_done, name='profile_done'),
    path('profile/create/', create, name='create'),
    path('profile/delete/<int:pk>', delete, name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
