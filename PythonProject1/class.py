class Human:
    def __init__(self, n, o, a):
        self.name = n
        self.occupation = o
        self.age = a

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots the film")

    def speaks(self):
        print(self.name, "says: How do you speak?")

    def eat_food(self):
        print(self.name, "eats the food")

# Create object
tom = Human("Tom Cruise", "actor", 61)
tom.do_work()
tom.speaks()
tom.eat_food()
aamair=Human("aamair","tennis player",97)
aamair.do_work()
aamair.speaks()
aamair.eat_food()