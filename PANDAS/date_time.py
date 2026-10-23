import pandas as pd
#single timestamp
ts = pd.Timestamp("2026-08-03 10:30:00")
print(ts)

print("--------------------------------------------------------")

#today's date/time
now=pd.Timestamp.now()
print(now)

print("--------------------------------------------------------")
#range of dates
date_range=pd.date_range(start='2026-01-01',end='2026-01-10',freq='D')
print(date_range)

print("--------------------------------------------------------")

#converting dates (pd.to_datetime)
dates_str=['2026-01-15','2026-03-25']
dates=pd.to_datetime(dates_str)
print(dates)

print("--------------------------------------------------------")

#custom string formats
df=pd.DataFrame({'date_str':['15/01/2026','20/02/2026','25/03/2026']})
df['date'] = pd.to_datetime(df['date_str'],format= '%d/%m/%Y')
print(df)
print("--------------------------------------------------------")

df['year']=df['date'].dt.year
print(df)
df['month']=df['date'].dt.month
print(df)
df['day']=df['date'].dt.day
print(df)
df['weekday_name']=df['date'].dt.day_name()
print(df)
df['month_name']=df['date'].dt.month_name()
print(df)
df['quarter']=df['date'].dt.quarter
print(df)

print('-------------------------------------------------------------------')
#simple formatting with.df.strftime()
df['formatted_1'] = df['date'].dt.strftime('%d-%m-%Y')
df['formatted_2'] = df['date'].dt.strftime('%B,%d,%Y')
print(df[['date','formatted_1','formatted_2']])
