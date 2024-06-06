import pandas as  pd

Sheet = pd.read_csv("ChildAtten.csv")
print(Sheet.to_string())

print(Sheet.head(10))

print(Sheet['Primary Age Group'].value_counts())
reg = Sheet[['Primary Event Type', 'Event Type Option 2']]
print(reg) 

Sheet.fillna(value = 20,inplace=True)

missing_values = Sheet.isna().sum()
print(missing_values)
Sheet.dropna(inplace=True)

Sheet['Attendance'].fillna(Sheet['Attendance'].mean(), inplace=True)
print(Sheet)

new_sheet = Sheet.drop_duplicates(subset=["Library",'Title'])
print(new_sheet.to_string())
Sheet.to_excel('output2.xlsx',index=False)
