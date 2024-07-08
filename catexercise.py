class Cat:
    li = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

cat1 = Cat("Sachi", 27)
cat2 = Cat("Abhi", 18)
cat3 = Cat("Vamshi", 28)


li = [ cat1.age, cat2.age, cat3.age]
    
print(f' the oldest cat in the group with age {max(li)}')




