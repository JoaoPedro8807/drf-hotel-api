from hotel.models import Room

def att_available_room(room_id: str, status:bool):
    room = Room.objects.get(id=room_id)
    room.available = status
    room.save()