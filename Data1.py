#list
Data =[11,21,51,101]
print("Data type is",type(Data))
print("Length of data is",len(Data))
print(Data)

print("Data from 0th index:",Data[0])
print("Data from 3rd index:",Data[3])

Data[0]=123


print("New 0th index:",Data[0])

Data.append(151)
print("Data from 4th index:",Data[4])

Data.insert(2,35)# list allow mutation
print(Data)

Data.insert(3,51)
print(Data)# list allow dupicate

Data.insert(5,3.14)
print(Data) #list allow Heteroginious Data


print(Data[-1])


print(Data[3:5])#range to display

i=0


print("Data using while loop")
while(i<len(Data)):
      print(Data[i])
      i=i+1

print("For loop:")
for i in range(len(Data)):
      print(Data[i])
