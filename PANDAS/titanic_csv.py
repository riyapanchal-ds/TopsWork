import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df)
import seaborn as sns
data_titanic = sns.load_dataset('titanic')
df=pd.DataFrame(data_titanic)
print(df)

print(df.shape)
print(df.index)
print(df.columns)
print(df.size)
print(df.info())
print(df.dtypes)

# print(df.describe())
# print(df.describe(include='object'))
# print(df.describe(include='all').T)
# print(df.sex.value_counts())
# print(df.sex.unique())
# print(df.sex.nunique())
# print(df.sex.value_counts().loc['male']/len(df)*100)
# print(df.sex.value_counts().iloc[0]/len(df)*100)
# print(df.deck.isnull().sum()/len(df)*100)
# # (df['age']=df.age.fillnadf.age.meadian())
# # df['age'] = df['age'].fillna(df['age'].median())
# print(df.embark_town.mode().iloc[0])
# print(df.embark_town.value_counts())
# print("----------------------------")
# df['embark_tow']=df.embark_town.fillna(df.embark_town.mode().iloc[0])
# print(df)
# print("----------------------------")
# print(df.head(10))
# print(df.tail(10))
# print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print(df.drop(columns=['embarked','class','who','adult_male','deck','alive','alone'],axis1=1,inplace=True))