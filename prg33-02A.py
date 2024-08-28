# Write code in Python with encapsulated class Employee(EId, Ename). Use inheritance for 
# implementation of 02 child classes EmployeeRegular(ESalary) and EmployeePartTime(EHours, 
# ERate). In main code, create 05 objects of both EmployeeRegular and Employee PartTime 
# classes, input their data, and display employee earning the highest salary.
class Employee():
    eid=0
    ename=""
    def __init__(self,eid=None,ename=None):
        if(eid==0):
            self.eid=0
            self.ename=""
        else:
            self.eid=eid
            self.ename=ename
    def SetData(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def InputData(self):
        self.eid=int(input("Give Employee I'D : "))
        self.ename=input("Give Employee Name : ")
    def DispData(self):
        print("Employee I'D = ",self.eid)
        print("Employee Name = ",self.ename)
    def GetEid(self):
        return self.eid
    def GetEname(self):
        return self.ename
    def __del__(self):
        print("Student Object Deleted")
class EmployeeRegular(Employee):
    Esalary=0
    def __init__(self,eid=None,ename=None,Esalary=None):
        if(eid==0):
            eid=0
            ename=""
            Esalary=0
        else:
            self.eid=eid
            self.ename=ename
            self.Esalary=Esalary
    def SetData(self,eid,ename,Esalary):
        Employee.SetData(eid,ename)
        self.Esalary=Esalary
    def InputData(self):
        Employee.InputData(self)
        self.Esalary=int(input("Give Employee Salary : "))
    def DispData(self):
        Employee.DispData(self)
        print("Employee Salary = ",self.Esalary)
    def GetEid(self):
        return Employee.GetEid(self)
    def GetEname(self):
        return Employee.GetEname(self)
    def GetEsalary(self):
        return self.Esalary
    def __del__(self):
        print("Employee Regular Object Deleted")
class EmployeePartTime(Employee):
    Ehours=0
    Erate=0
    def __init__(self,eid=None,ename=None,Ehours=None,Erate=None):
        if(Ehours==0):
            eid=0
            ename=""
            Ehours=0
            Erate=0
        else:
            self.eid=eid
            self.ename=ename
            self.Ehours=Ehours
            self.Erate=Erate
    def SetData(self,eid,ename,Ehours,Erate):
        Employee.SetData(eid,ename)
        self.Ehours=Ehours
        self.Erate=Erate
    def InputData(self):
        Employee.InputData(self)
        self.Ehours=int(input("Give Employee Hours : "))
        self.Erate=int(input("Give Employee Rate Per Hour : "))
    def DispData(self):
        Employee.DispData(self)
        print("Employee Hours = ",self.Ehours)
        print("Employee Rate Per Hour = ",self.Erate)
    def GetEid(self):
        return Employee.GetEid(self)
    def GetEname(self):
        return Employee.GetEname(self)
    def GetEhours(self):
        return self.Ehours
    def GetErate(self):
        return self.Erate
    def __del__(self):
        print("Employee Part Time Object Deleted")

ER=[]
for i in range(0,5):
    temp=EmployeeRegular()
    temp.InputData()
    ER.append(temp)
print("YOu Entered")
for i in range(0,5):
    ER[i].DispData()
loc=0
highest=ER[0].GetEsalary()
for i in range(1,5):
    if(ER[i].GetEsalary()>highest):
        highest=ER[i].GetEsalary()
        loc=i
print("Data of Employee Having Highest Salary is : ")
ER[loc].DispData()
EPT=[]
for i in range(0,5):
    temp2=EmployeePartTime()
    temp2.InputData()
    EPT.append(temp2)
print("*************You Entered***********")
for i in range(0,5):
    EPT[i].DispData()
