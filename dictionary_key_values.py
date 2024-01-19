#Emir Dostovic 
#Used chatGPT to figure out how to itterate through key value pairs in dictionaries
def get_combined_dict(a,b):
    c_dict={}
    for key in a:
        if key in b:
            c_dict[key]=a[key]+b[key]
    return c_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)