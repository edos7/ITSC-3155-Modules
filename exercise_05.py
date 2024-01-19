firstList=[]
secondList=[]
thirdList=[]
def is_unique(a, x):
    booler=True
    for num in range(len(a)):
        if(a[num]==x):
           return False
    return booler


for num in range(5):
    x=int(input("Please enter an Integer: "))
    firstList.append(x)
for num in range(5):
    x=int(input("Please enter an Integer: "))
    secondList.append(x)
for num in range(5):
    for num2 in range(5):
        if(firstList[num]==secondList[num2]):
            x=secondList[num2]
            if(is_unique(thirdList,x)):
                thirdList.append(x)

print(thirdList)    