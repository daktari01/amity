class Person:
    """
    Class for general person
    """
    def __init__(self, person_name):
        self.person_name = person_name


class Fellow(Person):
    """
    Class to define a fellow
    """
    def __init__(self, person_name):
        super().__init__(person_name)


class Staff(Person):
    """
    Class to define a staff
    """
    def __init__(self, person_name):
        super().__init__(person_name)

