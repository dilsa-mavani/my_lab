#basic default argument
def greet(name,msg="good morning"):
    print("hello",name+",",msg)
greet("Dilsa")
greet("bhumi","good morning")  
#power function
def power (num,exp=2):
    return num **exp
print(power(3))
print(power(3,3))
print(power(2,4)) 
#multiple default
def student_info(name,age=18,course="bscit"):
    print("name:",name)
    print("age:",age)
    print("course:",course)
student_info("DILSA")
student_info("SEEMA",20)
student_info("AMIT",20,"bsc.it")     