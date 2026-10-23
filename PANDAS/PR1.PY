import pandas as pd

name = pd.Series(["riya", "hani", "kavya"])
print(name)

# marks=pd.Series([85,90,78],index=["riya","hani","kavya"])
# print(marks)
# print(marks["riya"])

print(name.size)
print(name.shape)
print(name.ndim)
print(name.index)
print(name.values)
print(len(name))

#DATAFRAME  
df=pd.DataFrame({"a":[100,200,300],"b":[400,500,600],"c":[700,800,900],"d":[1000,1100,1200]})
print(df)
# df
