import websockets as websockets
from django.shortcuts import render

# Create your views here.
# import asyncio
#
# async def handler(websocket):
#     while True:
#         message = await websocket.recv()
#         print(message)
#
#
# async def test_view(request):
#     url = "wss://demo.piesocket.com/v3/channel_1?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self"
#     async with websockets.connect(url) as ws:
#         await handler(ws)
#         await asyncio.Future()  # run forever

def test_view(request):
    return render(request, 'test_socket/index.html')