# Write a program in python with class Product,create get,set,input and display functions,
#In main function create list of 10 Product objects and display input Data
class Product:
    pid=0
    pname=""
    qty=0
    def InputData(self):
        self.pid=int(input("Give PID"))
        self.pname=input("Give Product Name")
        self.qty=int(input("Give Quantity"))
    def DispData(self):
        print("Product ID ",self.pid)
        print("Product Name = ",self.pname)
        print("Quantity = ",self.qty)
    def SetData(self,pid,pname,qty):
        self.pid=pid
        self.pnameame=pname
        self.qty=qty
    def GetPid(self):
        return self.pid
    def GetPName(self):
        return self.pname
    def GetQty(self):
        return self.qty
    #Constructor in Python
    def __init__(self,pid=None,pname=None,qty=None):
        if(pid==None):
            pid=0
            pnameame=""
            qty=0
        else:
            self.pid=pid
            self.pname=pname
            self.qty=qty
    #Destructor in Python 
    def __del__(self):
        print("Object Deleted")
p=[]
for i in range(0,10):
    temp=Product()
    temp.InputData()
    p.append(temp)
for i in range(0,10):
    p[i].DispData()