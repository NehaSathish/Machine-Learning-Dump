import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
import math as m

def split(data):
    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])
    return x,y

def KNN(x,test_x,K):
    dist = []

    for i in range(len(x)):
        dist.append(m.sqrt((x[i][0] - test_x[0])**2 + (x[i][1] - test_x[1])**2 ))
    
    x_dist = list(zip(dist,x,y))
    x_dist.sort()
    
    count0 = 0
    count1 = 0
    
    for i in range(K):
        if(x_dist[i][2] == 0):
            count0 += 1
        elif(x_dist[i][2] == 1):
            count1 += 1
            
    if(count0 > count1):
        return 0
    elif(count1 > count0):
        return 1

wb = xl.open_workbook("data.xlsx")
sheet = wb.sheet_by_index(0)

data = []
x = []
y = []
y_name = ''
feature_name = []
K = 3

no_of_col = sheet.ncols


for i in range(no_of_col):
    data.append(sheet.col_values(i))

y.extend(data.pop(no_of_col-1))

y_name = y.pop(0)

for i in range(len(data)):
    feature_name.append(data[i].pop(0))

x = np.transpose(data).astype(int)

x0,y0 = [],[]
x1,y1 = [],[]
class0,class1 = [],[]
for i in range(len(x)):
    if(y[i] == 0):
        class0.append(x[i])
    elif(y[i] == 1):
        class1.append(x[i])

x0,y0 = split(class0)
x1,y1 = split(class1)


plt.scatter(x0,y0,c = 'r')
plt.scatter(x1,y1,c = 'g')

test_x = [6,1]

for i in range(1,8):
    test_y = KNN(x,test_x,i)
    print("For K = ",i,", the test data belongs to class ",test_y)


#print("Enter the test data : ")
#for i in range(len(feature_name)):
#    print("Enter the ",feature_name[i])
#    temp = int(input())
#    test_x.append(temp)
    
#print("For K = ",K,", the test data belongs to class ",test_y)
plt.scatter(test_x[0],test_x[1])
plt.legend(['Red = Class 0','Green = Class 1','Blue = Test Data'],loc = 'best')
