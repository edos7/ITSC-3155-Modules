def unique_list(a):
    unique_list=[]
    for x in range(len(a)):
        booler=True
        
        for j in range(len(a)):
            if(x==j):
                continue
            elif(a[x]==a[j]):
                booler=False
        if(booler==True):
            unique_list.append(a[x])
    return unique_list
my_list=[1,2,3,2,1,4]
u_list=unique_list(my_list)
print(u_list)