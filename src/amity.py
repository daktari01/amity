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
                print("Room {} already exists. Try with a different name".format(room))
                return
            if args['<room_type>'].lower() not in ['office', 'living']:
                print("Room type can only be office or living")
                return
            new_room = Office(room) if args['<room_type>'].lower == 'office' else LivingSpace(room)
            print(args['<room_type>'] + ' ' + ['<room_name>'] + 'created successfully')
            # if args['office']:
            #     new_room = Office(room)
            # else:
            #     new_room = LivingSpace(room)
                