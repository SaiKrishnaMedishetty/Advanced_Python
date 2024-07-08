class PlayerCharacter:
    membership = True #class object attribute
    def __init__(self, name):
        self.name = name # class attribute

    def shout(self): # using attributes you can perform certain action to it
        print(f' {self.name} is shouting...!')
        return "is it"


player1 = PlayerCharacter("Sachi")
print(player1.shout())