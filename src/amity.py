from src.rooms import Room, Office, LivingSpace

class Amity:
    """
    Implement room allocation logic
    """
    def __init__(self):
        self.all_rooms = []
        
    def create_room(self, args):
        for room in args['<room_name>']:
            if room.lower() in self.all_rooms:
                print("{} {} already exists. Try with a different name".format(
                    args['<room_type>'], room))
                return
            if args['<room_type>'].lower() not in ['office', 'living']:
                print("Room type can only be office or living")
                return
            new_room = Office(args['<room_type>'], room) if args[
                '<room_type>'].lower == 'office' else LivingSpace(args[
                    '<room_type>'], room)
            self.all_rooms.append(room.lower())
            print(args['<room_type>'] + ' ' + room + ' ' + 'created successfully')
            
                