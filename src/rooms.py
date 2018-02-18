class Room:
    """Class for general room"""
    def __init__(self, room_name, occupants, max_occupants):
        self.room_name = room_name
        self.occupants = occupants
        self.max_occupants = max_occupants

    def is_full(self, occupants, max_occupants):
        return True if self.occupants == self.max_occupants else False


class LivingSpace(Room):
    """Class LivingSpace inherits from class Room"""
    def __init__(self, room_name, occupants=0, max_occupants=4):
        super().__init__(room_name, occupants, max_occupants)


class Office(Room):
    """Class Office inherits from class Room"""
    def __init__(self, room_name, occupants=0, max_occupants=6):
        super().__init__(room_name, occupants, max_occupants)