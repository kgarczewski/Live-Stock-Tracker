from django.urls import path, include
from . import views as v
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', v.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', v.RegisterPage.as_view(), name='register'),
    path('', v.home, name='home'),
]