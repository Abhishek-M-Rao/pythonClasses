class Robot:
    #make constructor
    def __init__(self, name=None, color=None, weight=None):
        if name:
            self.name = name
            self.color = color
            self.weight = weight
        else:
            self.name = "default"
            self.color = "gray"
            self.weight = 0
            
    def introduce_self(self):
        print("My name is " + self.name) #this is like c "self" is kinda like "this" like pointer to the object

r1 = Robot(name = "Tom", color = "red", weight = 30)
r2 = Robot(name = "Jerry", color = "blue", weight = 40)
r3 = Robot()

r1.introduce_self()
r2.introduce_self()
r3.introduce_self()

#now second example - each person has a name, personaility, and isSitting or not - use function to change sit/stand up

class person:
    def __init__(self, name=None, personality=None, isSitting=None):
        if name:
            self.name = name
            self.personality = personality
            self.isSitting = isSitting
        else:
            self.name = "default"
            self.personality = "null"
            self.isSitting = False
    def sitdown(self):
        self.isSitting = True

    def standup(self):
        self.isSitting = False

    def introduction(self):
        print("My name is " + self.name)

    def sittingOrNot(self):
        if self.isSitting:
            print("I am sitting")
        else:
            print("I am standing")

    def myPersonality(self):
        print("I am a " + self.personality + " person")


p1 = person(name="Alice", personality="aggressive", isSitting=True)
p2 = person(name="Becky", personality="talkative", isSitting=False)
p3 = person()

p1.introduction()
p1.sittingOrNot()
p1.myPersonality()
p1.standup()
p1.sittingOrNot()




