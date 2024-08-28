#Introduction to OOP in Python
class MyClass:
    i = 0

    def method1(self):
        print("Method 1 called")
        self.i = 5

obj1 = MyClass() 
obj1.method1()
print("i =", obj1.i)
