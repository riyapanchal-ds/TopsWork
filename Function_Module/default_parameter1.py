#default parameter

def greet(name="Tops"):
    print("Good morning",name)
def square(no=1):
    return no*no
greet()
greet("riya")
print(square(20))
print(square(50))


def studentdetails(name,email,age=20):
    print(name,email,age)
studentdetails('riya','tst@gmail.com',22)
studentdetails('hani','tst@gmail.com')