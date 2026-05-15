def greet(name="Tops"):
    print("Good morning",name)
greet()
greet("riya")




#default parameter

def greet(name="Tops"):
    print("Good morning",name)
def square(no=1):
    return no*no
greet()
greet("riya")
print(square(20))
print(square())

