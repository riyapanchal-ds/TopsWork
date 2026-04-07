def unique_list(lst):
    result=[]
    for i in lst:
        if i not in result:
            result.append(i)

    return result
numbers=[1,2,2,3,4,4,5,6,6,7,6,8,9]
print(unique_list(numbers))