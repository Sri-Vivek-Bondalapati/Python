import csv
print('enter the ppath where text file is')
val = open("/Users/srivivek/Study/Python/realData.txt",mode = )
data = val.read()
daladec =data
eader = csv.reader(daladec, delimiter='\t')
for val in eader:
    print(val)
val.close()