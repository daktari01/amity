from src.rooms import Room, Office, LivingSpace
from src.people import Person, Staff, Fellow

class Amity:
    """
    Implement room allocation logic
    """
    def __init__(self):
        self.all_rooms = []
        self.all_people = []
        self.all_staff = []
        self.all_fellows = []
        
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
            print(args['<room_type>'] + ' ' + room + ' \
            ' + 'created successfully')
            
    def add_person(self, args):
        person_name = args['<first_name>'] + ' ' + args['<last_name>']
        if (args['<first_name>'].isalpha() or args['<last_name>'].isalpha()) == False:
            print("Names of people should contain alphabets only.")
            return
        
        # Check for duplicate entries YET TO WORK
        if person_name.lower() in self.all_people:
            print(person_name + " already exists. Try another one.")
            return
        
        if args['<person_type>'].lower() not in ['fellow', 'staff']:
            print("Person type can only be fellow or staff")
            return
        if args['<person_type>'].lower() == 'staff' and args[
            '<wants_accommodation>'] is not None:
            print("Staff cannot be allocated living spaces")
            return
        if args['<person_type>'].lower() == 'staff':
            new_person = Staff(person_name) 
            self.all_people.append(new_person)
            self.all_staff.append(new_person)
            print(person_name + " has been added as a " + args['<person_type>'] + " successfully.")

        if args['<wants_accommodation>'] not in [
            "N", "n", "no", "No", "Y", "Yes", None]:
            print("Wrong value for wants accommodation. \
                Use 'N', 'No', 'Y', 'Yes' or leave it blank")
            return
        
        # Fellow does not want accommodation
        if (args['<wants_accommodation>'] in ['n', 'N', 'no', 'No', None] and \
            args['<person_type>'].lower() == 'fellow'):
            new_person = Fellow(person_name)
            self.all_people.append(new_person)
            self.all_fellows.append(new_person)
            print(person_name + " has been added as a " + \
                args['<person_type>'] + " successfully.")
        
        # Fellow wants accommodation
        elif (args['<wants_accommodation>'] in ['y', 'Y', 'yes', 'Yes', 'YES'] \
            and args['<person_type>'].lower() == 'fellow'):
            new_person = Fellow(person_name, 'Y')
            self.all_people.append(new_person)
            self.all_fellows.append(new_person)
            print(person_name + " has been added as a " + \
                args['<person_type>'] + " successfully.")


                