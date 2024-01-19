def is_unique(a,x,y): 
    for num in range(len(a)):
        if(a[num]==x and num!=y):
           return False
    return True
originalList=[]
uniqueList=[]
for num in range(10):
    x=int(input(f"Enter number #{num+1}: "))
    originalList.append(x)
for num in range(len(originalList)):
    if(is_unique(originalList,originalList[num],num)):
        uniqueList.append(originalList[num])

print(originalList)
print(uniqueList)
          
                
          
