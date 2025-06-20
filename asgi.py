import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import blog.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_platform.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                blog.routing.websocket_urlpatterns
            )
        ),
    }
)
