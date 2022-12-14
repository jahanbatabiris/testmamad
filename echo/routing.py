from django.urls import path
from echo import consumers

websocket_urlpatterns = [
    path('ws/', consumers.EchoConsumer.as_asgi(), name='echo'),
    path('ws/chat/<str:username>/', consumers.ChatConsumer.as_asgi(), name='chat'),
]
