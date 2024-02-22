"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from django.urls import path
from core.consumer import ProgressConsumer

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        "websocket": AuthMiddlewareStack(URLRouter([
         path("ws/progress/<task_id>", ProgressConsumer.as_asgi()),
        ]))
    }
)