import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df)

import seaborn as sns
data_titanic = sns.load_dataset('titanic')
df = pd.DataFrame(data_titanic)

print(df)

# import sqlite3

# conn = sqlite3.connect(":memory:")
# df.to_sql("df", conn, index=False, if_exists="replace")
# query = "SELECT * FROM df"
# df_sql = pd.read_sql_query(query, conn)
# print(df_sql)
# print("---------------------------------------------")

# query="select sex,pclass,survived,age,fare from df where age>30 limit 10"
# df_sql = pd.read_sql_query(query, conn)
# print(df_sql)

# print("---------------------------------------------")

# from sqlalchemy import create_engine

# engine = create_engine(
#     "mysql+pymysql://root:@localhost:3306/student_db"

# )
# print(engine)

# print("---------------------------------------------")

# import requests
# resonse=requests.get("https://api.exchangerate-api.com/v4/latest/INR")
# data=resonse.json()
# df3=pd.DataFrame(data['rates'],index=[0])
# print("JSON file created successfully.")
# print(df3.T)

# print("---------------------------------------------")

import pathlib

data_dir = pathlib.Path("titanic_project")/ "data"
data_dir.mkdir(exist_ok=True, parents=True)
csv_path = data_dir / "titanic.csv"
df.to_csv(csv_path, index=False)
print(csv_path.resolve())
print(csv_path.exists())
print(csv_path.name)
print(csv_path.parent)
print(csv_path.suffix)

# sample=df[["embark_town"]].iloc[:10].copy()
# print(sample)
# sample=df[["embark_town"]].iloc[:10].copy()
# sample["ffill"]=sample["embark_town"].ffill() #forwardfill
# sample["bfill"]=sample["embark_town"].bfill()  #backward fill
# print(sample)
# print(pd.crosstab(df.sex,df.survived))
# print(pd.crosstab(df.sex,df.survived,normalize=True)*100)     #percentage me dekhna hon to

# result=df["sex"]=pd.get_dummies(df.sex,drop_first=True,dtype=int)          #encoding
# print(result)
# df['embark_town'] = df['embark_town'].map({
#     "Southampton": 0,
#     "Cherbourg": 1,
#     "Queenstown": 2
# })

# print(df['embark_town'])
# print(df)

