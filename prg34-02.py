# write program in python to store students data to a binary file.
# write code t read entire data from binary file and display it
class Student:
    rollno=0
    name=""
    marks=0
    def __init__(self,rollno=None,name=None,marks=None):
        if(rollno==None):
            rollno=0
            name=""
            marks=0
        else:
            self.rollno=rollno
            self.name=name
            self.marks=marks
    def SetData(self,rollno,name,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
    def InputData(self):
        self.rollno=int(input("Give Roll No"))
        self.name=input("Give Name")
        self.marks=int(input("Give Marks"))
    def dispData(self):
        print("Roll no = ",self.rollno)
        print("Name = ",self.name)
        print("Marks = ",self.marks)
    def GetRollno(self):
        return self.rollno
    def GetName(self):
        return self.name
    def GetMarks(self):
        return self.marks 
    def __del__(self):
        print("Object Deleted")
s = Student()
s2=Student(1,"abc", 78)
s.dispData()
s2.dispData()
import pickle
fp = open('student.bin','wb')
pickle.dump(s, fp, pickle.DEFAULT_PROTOCOL)
pickle.dump(s2, fp, pickle.DEFAULT_PROTOCOL)
print("***Written objects to file**")
fp.close()
print("****** Student File Data *****")
try:
 fp2 = open('student.bin','rb')
 s= pickle.load(fp2)
 while s:
  s.dispData()
  s = pickle.load(fp2)
except EOFError:
 pass 
fp2.close()