# Write a program in python with class Student,create get,set,input and display functions,In main function create 2 objects and display input Data
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
    def __del__(self):
        print("Object Deleted")
s=Student()
s2=Student(10,"abc",3)
s.DispData()
s2.DispData()