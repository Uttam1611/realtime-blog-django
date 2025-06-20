from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/posts/', consumers.PostsConsumer.as_asgi()),  # Real-time post updates
]