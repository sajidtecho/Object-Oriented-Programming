#initiate a class
class employee:
    #constructor
    def __init__(self):
        print("Started executing attributes")
        self.name="Sajid"
        self.salary=50000
        self.id=123
        print("Attributes are initialized successfully")
        
    #creating a method
    def travel(self,destination):
        print("I am travelling to office in",destination)
      
# creat an object of the employee class
emp1 = employee() 

# print(emp1.name) 
# print(emp1.salary)
# print(emp1.id)

# call the method using the object
emp1.travel("bangalore")

print(type(emp1))

    