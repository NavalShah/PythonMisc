class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


person1 = Person("John", "Wick")
person1.printname()

class Child(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


child1 = Child("Naval", "Shah", 2026)
child1.welcome()

class Baby(Child):
    def __init__(self, fname, lname, year, age, personality, iq):
        super().__init__(fname, lname, year)
        self.yearsofage = age
        self.personality = personality
        self.intelligence = iq

    def introduction(self):
        print("Hello young", self.firstname, self.lastname, " how are ya!!\n"
              "you don't need to worry about high school yet,\n"
              "but if all goes well, you will graduate in:", self.graduationyear,
              "You are currently", self.yearsofage)

child1 = Baby("Naval", "Shah", 2026, 14, "introverted", 129)
child1.introduction()


