from django.urls import path
from .views import users,get_content


app_name = "Validation"

urlpatterns = [
    path('users/',users,name="users"),
    path('connect/',get_content,name='FastAPi'),

]
