             
               ########### Bike Rental System - Python Project ###########

class bikeShop:
               
               def __init__(self,stock):
                       self.stock = stock
               def displayBike(self):
                       print("Total Bike",self.stock)
               def rentForBike(self,q):
                       
                       if q <= 0:
                               print("Enter the positive value or greater than zero ")
                       if q>self.stock:
                               print("enter the value (less then stock)")
                       else:
                               self.stock = self.stock - q
                               print("Total prices: ",q * 100)
                               print("Total Bikes: ",self.stock)
                       

while True:
        obj = bikeShop(100)
        user_choice =  int(input('''  

1 Display Stocks
2 Rent a bike
3 Exit
                         '''))
        if user_choice == 1:
                obj.displayBike()
        elif user_choice == 2:
                n = int(input("Enter the Qty:--- "))
                obj.rentForBike(n)
        else:
                break