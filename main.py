class car:
    def __init__(self, company, type):
        self.company = company
        self.type = type

    def info(self):
        print("The car information is: ",self.company, self.type)

comp1 = car("maruti", "Petrol")
comp2 = car ("Skoda", "EV")

comp1.info()
comp2.info()
