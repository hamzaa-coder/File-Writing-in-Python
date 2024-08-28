# Write a program in python with class Student,create get,set,input and display functions,
#In main function create list of 10 Student objects and display input Data
class Student:
    rollno=0
    name=""
    marks=0
    def InputData(self):
        self.rollno=int(input("Give Roll No"))
        self.name=input("Give Name")
        self.marks=int(input("Give Marks"))
    def DispData(self):
        print("Roll no = ",self.rollno)
        print("Name = ",self.name)
        print("Marks = ",self.marks)
    def SetData(self,rollno,name,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
    def GetRollno(self):
        return self.rollno
    def GetName(self):
        return self.name
    def GetMarks(self):
        return self.marks
    #Constructor in Python
    def __init__(self,rollno=None,name=None,marks=None):
        if(rollno==None):
            rollno=0
            name=""
            marks=0
        else:
            self.rollno=rollno
            self.name=name
            self.marks=marks
    #Destructor in Python 
    def __del__(self):
        print("Object Deleted")
s=[]
for i in range(0,10):
    temp=Student()
    temp.InputData()
    s.append(temp)
for i in range(0,10):
    s[i].DispData()