from django.urls import path
from .views import users,get_content
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
app_name = "Validation"

urlpatterns = [
    path('users/',users,name="users"),
    path('connect/',get_content,name='FastAPi'),
    path('token/',TokenObtainPairView.as_view(),name='Token_obtain_view'),
    path('token/refresh/',TokenRefreshView.as_view(),name='Token_Refresh_View'),
    
]
