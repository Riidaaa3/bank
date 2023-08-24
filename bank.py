import time
database={}

class bank:
    def __init__(self,name,balance):
       self.name=name
       self.balance=balance
       database.update({name:balance})

    def deposit(self):
        amount=int(input("enter the deposit amout:"))
        if amount>0:
            self.balance+=amount
            print("succesuful transaction.\nNew balance:"+str(self.balance))
            database[self.name]=self.balance 
        else:
            print("unsuccessful transaction.\nTry again")    
    def withdraw(self):
        amount=int(input("enter the windowaw amount:"))
        if amount<=self.balance and amount >0:
           self.balance-=amount
           print("successufl transaction.\nNew balance:"+str(self.balance))
        else:
           print("unsuccessful transaction.\nTry again")  
    def translfer(self):
        receiver=input("enter the name of receiver:")
        if receiver in database.keys() and receiver!=self.name:
           amount=int(input("enter the amount:"))
           if amount<=self.balance:    
            self.balance-=amount
            database[self.name]=self.balance
            print(f"successful transation\n{str(amount)}transferred to{receiver}\n your new balance:{self.balance}")


           else:
            print("unsuccessful transaction.try again")    
        else:
           print("ba2olk try again ba2a")       