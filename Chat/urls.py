from django.urls import path
from .views import Chat,Upload

app_name = "Chat"

urlpatterns = [
    path('sky/text/',Chat),
    path('upload/',Upload),
]