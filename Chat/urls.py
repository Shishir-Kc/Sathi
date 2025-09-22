from django.urls import path
from .views import Chat
app_name = "Chat"

urlpatterns = [
    path('sky/text/',Chat),

]
