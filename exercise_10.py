x=input("Enter a string: ")
list=[]
listOfLists=[]

for i in range(len(x)):
    list.append(x[i])
    if(len(list)==3):
        listOfLists.append(list)
        list=[]

    if(i+1==len(x)):
        listOfLists.append(list)
print(listOfLists)