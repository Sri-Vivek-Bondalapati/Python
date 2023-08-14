import pandas as pd

path ='/Users/srivivek/Study/Python/test.xlsx'
df = pd.read_excel(path, sheet_name=0) #reads the first sheet of your excel file
print(df[df.columns[0]].count())
df_1 =df
df_1.drop_duplicates(subset="asin",keep="first", inplace=True)
print(df[df.columns[0]].count())
writer = pd.ExcelWriter('outputReport.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'raw')
df_1.to_excel(writer, sheet_name = 'uniques')
writer.close()
#df_6.to_excel(path,sheet_name='Unique')
'''df2=df.query("destination_country_code' == 'CN'")
print('added filter')
print(df2.info())
df.to_excel('test.xlsx', sheet_name='Unique') #Saving to a new sheet called Filtered Data
'''