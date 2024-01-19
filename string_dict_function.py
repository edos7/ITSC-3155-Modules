#Emir Dostovic 
def string_dictionary(a):
    my_dict={}
    collect_unique_values(a)
    for x in range (len(unique_keys)):
        my_dict[unique_keys[x].lower()]=unique_counter(a, unique_keys[x])
    return my_dict
def collect_unique_values(a):
    for x in range(len(a)):
        if(a[x] not in unique_keys):
            if(a[x]!=" "):
                unique_keys.append(a[x])


def unique_counter(a,b):
    counter=0
    for x in range(len(a)):
        if(a[x]==b):
            counter+=1
    return counter

unique_keys=[]
userInput=input("Enter a string: ")
string_dict=string_dictionary(userInput)       
print(string_dict)       
        
