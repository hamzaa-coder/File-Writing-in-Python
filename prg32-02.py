class Student:
    def __init__(self, rollno=0, name=""):
        self.rollno = rollno
        self.name = name

    def SetData(self, rollno, name):
        self.rollno = rollno
        self.name = name

    def InputData(self):
        print("Give Data")
        self.rollno = int(input("Enter Roll Number: "))
        self.name = input("Enter Name: ")

    def DispData(self):
        print("****************")
        print("Roll Number =", self.rollno)
        print("Name =", self.name)

    def GetRollno(self):
        return self.rollno

    def GetName(self):
        return self.name

    def __del__(self):
        print("Object Destroyed")

class StudentBSC(Student):
    def __init__(self, rollno=0, name="", fscMarks=0):
        super().__init__(rollno, name)
        self.fscMarks = fscMarks

    def SetData(self, rollno, name, fscMarks):
        super().SetData(rollno, name)
        self.fscMarks = fscMarks

    def InputData(self):
        super().InputData()
        self.fscMarks = int(input("Give FSC Marks: "))

    def DispData(self):
        super().DispData()
        print("FSC Marks =", self.fscMarks)

    def GetFscMarks(self):
        return self.fscMarks

    def __del__(self):
        print("Student BSC Object Deleted")

class StudentMCS(Student):
    def __init__(self, rollno=0, name="", bscMarks=0):
        super().__init__(rollno, name)
        self.bscMarks = bscMarks

    def SetData(self, rollno, name, bscMarks):
        super().SetData(rollno, name)
        self.bscMarks = bscMarks

    def InputData(self):
        super().InputData()
        self.bscMarks = int(input("Give BSC Marks: "))

    def DispData(self):
        super().DispData()
        print("BSC Marks =", self.bscMarks)

    def GetBscMarks(self):
        return self.bscMarks

    def __del__(self):
        print("Student MCS Object Destroyed")

sb1 = StudentBSC()
sb1.InputData()
sb1.DispData()

sb2 = StudentBSC(2, "pqr", 96)
sb2.DispData()

sm1 = StudentMCS()
sm1.InputData()
sm1.DispData()

sm2 = StudentMCS(4, "xyz", 98)
sm2.DispData()