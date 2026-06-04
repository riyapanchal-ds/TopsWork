# # oops in python
# #student details

# #USING LIST
# student_1 = ['madhav' ,10] #name,class
# student_2 =['kavya', 12]
# student_3 =['mital',22]
# #print(student_1[0])
# print(f'{student_3[0]} is in class {student_1[1]}')
# print(f'{student_2[0]} is in class {student_2[1]}')
# print(f'{student_1[0]} is in class {student_3[1]}')



# #USING OOPS
# #class :-- blueprint or template
# class student:
#     name = 'riya'
#     age=22

# # object :-- instance of class
# student1 = student()       #student class nu name che 
# print(student1.age , student1.name)

#student class
# class student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade} ,with {self.percentage} percentage%")

# student1=student('madhav',11,91)

# student2=student('riya',21,90)
# print(student1.name)
# student1.student_details()
# student2.student_details()

# print(student1.__dict__)  #dictonary form ma vallue key and value pair

# #studennt1 ma percentage change karva
# print(student1.percentage)
# student1.percentage =97 #modify 
# print(student1.percentage)

# #delete object properties
# print(student1.__dict__)
# del student1.percentage
# print(student1.__dict__)

# #delete object
# del student1       #delete ho jaega student1
# print(student1)

        


####ex2
class student:
    def __init__(self,name,grade,percentage,team):
        self.name=name
        self.grade=grade
        self.percentage=percentage
        self.team=team


    def student_details(self):
        print(f"{self.name} is in class {self.grade} ,with {self.percentage}% is in team {self.team}")
team1 = 'A'
team2 = 'B'
student1=student('madhav',11,91,team1)

student2=student('riya',21,90,team2)
print(student1.team)
print(student2.team)

student1.student_details()
student2.student_details()


#OOPS features
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

#ABSTRACTION - important details ne batavse nd unneccesary details ne hide karse
class student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage
      


    def student_details(self):
        print(f"{self.name} is in class {self.grade} ,with {self.percentage+2}% ")  #hidden from user 

student1=student('madhav',11,91)

student2=student('riya',21,90)

student1.student_details()


#encapsulation : secure kare data ne 
class student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.__percentage=percentage  #use double underscore 
   
   
   
    def get_precentage(self):     #restrict karse matalb avi rite use kari sakase
        return self.__percentage



    def student_details(self):
        print(f"{self.name} is in class {self.grade} ,with {self.percentage}% ")  

student1=student('madhav',11,91)

student2=student('riya',21,90)

# student.student_details()
# print(student1.__percentage)  #error aapse 
# print(student1.percentage)   #error aapse 

print(student1.get_precentage())


#inheritance :one class properties use another class

 #Parent class---BAAP
class student:    #BAAP
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage
      


    def student_details(self):
        print(f"{self.name} is in class {self.grade} ,with {self.percentage}% ")  #hidden from user 

student1=student('madhav',11,91)
student2=student('riya',21,90)

#child class --- beta
class graduatestudent(student):      #student parents class che curly breaket ma 
    def __init__(self, name, grade, percentage,stream):        #old parameter for parents class and new parameter 
        super().__init__(name, grade, percentage)     #supper etle parents class
        self.stream=stream#new attribute
grad_student1=graduatestudent('keshav',12,96,'PCM')
print(grad_student1.stream)
print(student1.percentage)