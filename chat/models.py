from django.db import models
from django.contrib.auth.models import User

import random
import string

# Create your models here.
class rooms(models.Model):
    room_name = models.CharField(max_length = 20)
    @classmethod
    def create_room(cls):
        symbols = '0123456789abcdefghijklmnopqrstuvwxyz' + string.ascii_uppercase
        x = True
        while x:
            name = ''.join(random.choice(symbols) for _ in range(20))

            try:
                 rooms.objects.get(room_name = name)
            except:
                cls.objects.create(room_name = name)

                return cls.objects.get(room_name = name)

class connections(models.Model):
    room = models.OneToOneField(rooms,on_delete = models.CASCADE)
    current_user = models.ForeignKey(User, related_name='chat', null=True,on_delete=models.CASCADE)
    connected_user =  models.ForeignKey(User, related_name='chat_connected_user', null=True,on_delete=models.CASCADE)


    @classmethod

    def make_room(cls, current_user, connected_user):

     while True:
        try:
            connection = cls.objects.get(current_user = current_user, connected_user = connected_user)
        except:
            connected_room = rooms.create_room()
            connection = cls.objects.create(current_user = current_user, connected_user = connected_user,room = connected_room)
            return
    @classmethod

    def loose_room(cls, current_user, connected_user):

        try:
            connection = cls.objects.get(current_user = current_user, connected_user = connected_user)
        except:
            connection = cls.objects.get(current_user = connected_user, connected_user = current_user)
        connection.room.remove(connection.room)
# try:
#     connection = b.objects.get(current_user = u, connected_user = v)
# except:
#     connection = b.objects.create(current_user = u, connected_user = v)
#     connected_room = rooms.create_room(u)
#     connection.room.add(connected_room)
