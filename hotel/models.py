from django.db import models
import uuid
from django.conf import settings



class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC ROOM'),
        ('NAC', 'NON-AC ROOM'),
        ('DEL', 'DELUXE ROOM'),
        ('KIN', 'KING ROOM'),
        ('QUE', 'QUEEN ROOM'),
        ('STE', 'SUITE ROOM'),
    )
    number = models.IntegerField()
    category =models.CharField(max_length=3,choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    
    def __str__(self):
        return f'Room Num- {self.number} : {self.category}, Beds = {self.beds} , People = {self.capacity}'
    
    
class Booking(models.Model):
    id = models.UUIDField(
        primary_key=True,default=uuid.uuid4, unique=True, editable= False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    
    def __str__(self):
        return f'{self.user} booked Room Num-{self.room.number} from = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}'