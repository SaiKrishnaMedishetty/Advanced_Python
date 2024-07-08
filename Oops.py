class User:
    def sign_in(self):
        print("logged in")

class killer(User): #inheritance
    def __init__(self, name, weapons):
        self.name = name
        self.weapons = weapons

    def action(self): #Polymorphism
        print(f'the {self.name} killer is going to kill the victim with his {self.weapons} weapon')

class Victim(User): #inheritance
    def __init(self, name):
        self.name = name
    
    def action(self): #Polymorphism
        print(f" The {self.name} Victim is running to save his life")

killer1 = killer("abhi","knife")
killer1.action()
# killer1.sign_in()