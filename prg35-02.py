# write program in python to store students data to a binary file into list of objects.
# write code t read entire data from binary file and display it and display data of student with highest marks
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
    def setData(self,rollno,name,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
    def inputData(self):
        self.rollno=int(input("Give Roll No"))
        self.name=input("Give Name")
        self.marks=int(input("Give Marks"))
    def dispData(self):
        print("Roll no = ",self.rollno)
        print("Name = ",self.name)
        print("Marks = ",self.marks)
    def getRollno(self):
        return self.rollno
    def getName(self):
        return self.name
    def getMarks(self):
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
ar1=[]
try:
 fp2 = open('student.bin','rb')
 s= pickle.load(fp2)
 while s:
  s.dispData()
  ar1.append(s)
  s = pickle.load(fp2)
except EOFError:
 pass 
except:
 print("Error in processing file")
fp2.close()
for i in range (0,len(ar1)):
 ar1[i].dispData()
highest=ar1[0].getMarks()
loc=0
for i in range (1,len(ar1)):
 if ar1[i].getMarks()>highest:
  highest = ar1[i].getMarks()
  loc = i
print("******Data of student with highest marks****")
ar1[loc].dispData()


# Assignment of same program but in product scenerio...