import math
import csv

from numpy import number

with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data= file_data[0]

def mean():
    m = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/m
    return mean

squared_list = []
for num in data:
    a = int(num) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for t in squared_list:
    sum = sum+i

result = sum/(len(data)-1)
standardDeviation=math.sqrt(result)
print(standardDeviation)