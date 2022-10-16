import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room


class EchoConsumer(WebsocketConsumer):
    def connect(self):

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            self.send(text_data=text_data + " - Sent By Server")
        elif bytes_data:
            self.send(bytes_data=bytes_data)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['username']
        all_rooms = Room.objects.all()
        free_rooms = Room.objects.filter(connected_user__lt=4,is_started=False)
        if not all_rooms.exists():
            new_room = Room()
            new_room.room_group_name= "room_1"
            new_room.code = self.room_name
            new_room.save()
            self.room = new_room
        else:
            if free_rooms.exists():
                self.room = free_rooms.first()
                self.room.connected_user = self.room.connected_user + 1
                if self.room.connected_user == 4 :
                    self.room.is_started = True
                self.room.save(update_fields=['connected_user',"is_started"])

            else:
                group_name = all_rooms.count()+1
                new_room = Room()
                new_room.room_group_name = f"room_{group_name}"
                new_room.code = self.room_name
                new_room.save()
                self.room = new_room

        self.room_group_name = self.room.room_group_name
        print(self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        self.room = Room.objects.filter(room_group_name=self.room_group_name).first()
        if self.room.connected_user -1 == 0:
            Room.objects.filter(room_group_name=self.room_group_name).delete()
        self.room.connected_user = self.room.connected_user - 1
        self.room.save(update_fields=['connected_user'])

    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            username = text_data_json['receiver']
            user_group_name = self.room_group_name

            async_to_sync(self.channel_layer.group_send)(
                user_group_name,
                {
                    'type': 'chat_message',
                    'message': text_data
                }
            )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=message)
