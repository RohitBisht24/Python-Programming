class BankAccount:
    def __init__(self, name, balance):
        self.name = name    #public
        self.__balance = balance  #private

    def get_balance(self):  #getter
        return self.__balance

    def set_balance(self, newBalance):  #setter
        self.__balance = newBalance


acc1 = bankAccount("rahul Kumar", 100_000)

# print(acc1.name, acc1.__balance)

acc1.set_balance(200_000)  # for set
print(acc1.name, acc1.get_balance())  # for get

# dusra tareeka
# print(acc1.name, acc1._BackAccount__balance()) 
