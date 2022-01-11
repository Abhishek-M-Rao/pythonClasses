# print("hello world!")
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
