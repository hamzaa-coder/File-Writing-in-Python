# Write Program in python with class Book,create get,set,disp and input functions
# in main Function create 10 Book Objects and display data of Book with highest price
class Book:
    bid=0
    name=""
    price=0
    def __init__(self,bid=None,name=None,price=None):
        if(bid==None):
            bid=0
            name=""
            price=0
        else:
            self.bid=bid
            self.name=name
            self.price=price
    def SetData(self,bid,name,price):
        self.bid=bid
        self.name=name
        self.price=price
    def InputData(self):
        self.bid=int(input("Give Bid"))
        self.name=input("Give Name")
        self.price=int(input("Give Price"))
    def DispData(self):
        print("Book Id = ",self.bid)
        print("Name = ",self.name)
        print("Price = ",self.price)
    def GetBid(self):
        return self.bid
    def GetName(self):
        return self.name
    def GetPrice(self):
        return self.price
    def __del__(self):
        print("Object Destroyed")
b=[]
for i in range(0,10):
    temp=Book()
    temp.InputData()
    b.append(temp)
loc=0
highest=b[0].price
for i in range(1,10):
    if(b[i].GetPrice()>highest):
        highest=b[i].price
        loc=i
print("Book with Highest Price is : ")
b[loc].DispData()
