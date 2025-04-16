from django.contrib import admin
from django.urls import path 
from . import views
from .views import chatbot_page, chatbot_response

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login_register_view, name='login_register_view'),
    path('start/', chatbot_page, name='chatbot_page'),  # ✅ Frontend page
    path('get_response/', chatbot_response, name='chatbot_response'),  # ✅ API route
]