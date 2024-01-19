array=[[0]* 5 for _ in range(5)]

x=int(input("Enter a row num from 1 to 5: "))
y=int(input("Enter a column num from 1 to 5: "))
array[x-1][y-1]=1

for element in array:
    print(element)