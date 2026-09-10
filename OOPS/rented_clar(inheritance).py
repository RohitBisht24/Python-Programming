# Q. Create Vehicle → Car → RentalCar.
#     Implement:
#     • rent a car for a number of days
#     • return the car
#     • prevent renting the same car twice
#     • calculate rental cost
#     • add a late-return fine


class Vehicle:
    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self,model,number):
        self.model = model
        self.number = number
        brand = input("Enter brand: ")
        super().__init__(brand)

class Rental_Car(Car):
    def __init__(self):
        model = input("Enter model number: ")     
        number = input("Enter number: ")
        super().__init__(model,number)
        self.rented = False
        self.days = 0
        
        self.cost = self.calc_cost()
        


    def rent_car(self):
        if (self.rented==False):
            self.rented = True
            self.rent = input("Enter rent of one day: ")
            self.days = int(input("For how many days would you like to rent the car: "))
            print("Cost:",self.days*self.rent)
            # self.cost = self.rent*self.days
            print("Car rented\n")
        else:
            print("The car is already rented\n")            

    def return_car(self):
        self.late_return = bool(int(input("Enter 1 if late return else 0: ")))
        if (self.rented):
            self.rented = False
            print("Bill:")
            self.calc_cost()                    
            print(self.cost)

        else:
            print("The car is not rented\n")
    
    def calc_cost(self):
        if (self.late_return):
            self.cost = self.rent*self.days*1.2
        else:
            self.cost = self.rent*self.days

car1 = Rental_Car()
car1.rent_car()            
car1.return_car()