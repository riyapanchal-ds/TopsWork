# 1. Arithmatic operators
'''a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a%b)

# 2. comparision operators
a=5
b=3
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# 3.Assignment operators
a = 5      #assignment operators

#4. logical operators
a=10
b=20

#Rule for 'and' operator
#true + true=False
#True + false=False
#False + False=False
print(a>10 and b<10) #and operator

#Rule for 'or' operators
#true + false = true
print(a==10 or b<10) #or operators

#NOT operators reverse outpput dega
print(not(a==10 and b==10))'''

#. identity operators  -->is ,not is
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)
print(x is z)

print(x is not z)#is not

# 6. Membership operator
my_list = ['apple','banana','orange']
print('apple' in my_list)
print('watermelon' in my_list)
print('apple' not in my_list) #not in operators

#7.Bitwise operators  -->AND&, OR| , XOR^ , NOT~ , ETC
a=5           # 5 in binary- 0101
b=3           # 3 in binary- 0011 
print(a & b)  # 1 in binary- 0001

#Rule for 'AND' '&' operator
#true + true=False
#True + false=False
#False + False=False