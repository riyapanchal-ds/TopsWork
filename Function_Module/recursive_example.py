#factorial

def factorial(n):
    #for i in range(1,n+1):
     #   fact*=i
      #  return fact

      if n==1:
            return 1
      else:
            print("else",n)
            return n*factorial(n-1)
print(factorial(5))

def print_numbers(n):
      if n==0:
            return
      print_numbers(n-1)
      print(n)
print_numbers(5)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))