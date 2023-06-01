from . import views
from django.urls import path

urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('turkey',views.turkey,name='turkey'),
    path('book',views.book,name='book'),\
    path('booknow',views.booknow,name='booknow'),


]
