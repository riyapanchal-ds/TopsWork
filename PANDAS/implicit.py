import pandas as pd
df=pd.DataFrame({"a":[100,200,300],"b":[400,500,600],"c":[700,800,900],"d":[1000,1100,1200]})
print(df)
print(df.iloc[1]) #implicit index
df.index=["x","y","z"]  #explicit index
print(df)   #explicit index
print(df.iloc[1]) #implicit index
print(df.loc["y"])  #explicit index
print(df.loc["x":: 2])#explicit index
print(df.iloc[:: 2]) #implicit index

#meanian


# df = pd.read_csv(url)

# print(df)