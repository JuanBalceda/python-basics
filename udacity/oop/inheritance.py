class Parent:
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_toys = number_toys

    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)
        print("Number of toys - " + str(self.number_toys))


billy = Parent("Rocket", "blue")
# print(billy.last_name)

sophie = Child("Flowers", "green", 5)
# print(sophie.last_name)

billy.show_info()
sophie.show_info()
