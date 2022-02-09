import csv

with open('Height-Weight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

r = len(new_data)
new_data.sort()
if r % 2 == 0:
    median1=float(new_data[r//2])
    median2=float(new_data[r//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[r//2] 


print("median" + str(median))
