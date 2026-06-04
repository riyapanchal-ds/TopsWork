#1.REQUIRED ARGUMENNTS
# def greetings(name):              #name is parameter
#     print("hello", name , "!")
# #greetings()  #value aapvi j pade niter error ape ene required argumnet kevay
# greetings("riya")              #riya is argument
#                                       #jetla parameter etli argument
# def intro(course_name, insructor_name):
#     print("welcome to",course_name,"course by",insructor_name)
# intro("python","riya")

#2.DEFAULT ARGUMENTS
# def greetings(name = "world"):              #name is parameter
#     print("hello", name , "!")
# #greetings()                #runs without errors using default value
# greetings("riya")



#3. KEYWORD ARGUMENT
# def divide(a,b):
#     return a/b
# result1 = divide(100,20)         #positional argument
# print(result1)

# result2 = divide(b=100,a=20)         #keyword argument
# print(result2)


#4.VARIABLE ARGUMENT
#store arguments in tuple
# def add2numbers(a,b):
#     return a+b
# result = add2numbers(3,5)
# print(result)

# def add3numbers(a,b,c):
#     return a+b+c
# result1 = add3numbers(3,5,1)              #isko hume alg alg likhna padta he
# print(result1)

# #args-->store arguments in tuple

# def add_numbers(*args):
#     return sum(args)
# output = add_numbers(1,2,3)                #yaha par jitne chahe uske argument pass kar sakte he
# print(output)

# def greetings2(*names):
#     for name in  names:
#         print(f"hello,{name}!")
# greetings2("madhav","riya")

#kwargs-->store arguments in dictonary
def print_details(**kwargs):
    print (type(kwargs))          #dictionary type
    for key ,value in kwargs.items():
        print(f"{key}:{value}")
        
print_details(name = "madhav", age = 20, city = "surat")