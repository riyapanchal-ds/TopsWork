#yield  vs return difference
def my_Generator():
  for i in range(6):
    yield i
#ans = my_Generator()
ans=my_Generator()
#print(ans)
#for i in ans:
 # print(i)
print(ans.__next__())