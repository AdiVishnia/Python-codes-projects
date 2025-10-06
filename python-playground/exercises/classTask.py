class Person:
    def __init__(self,firstname,surname):
        self.firstname=firstname
        self.surname=surname
    def full_name(self):
        print(f"first name: {self.firstname} surname: {self.surname}")

new_person=Person("Adi","Vishnia")
new_person.full_name()