import math

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = my_list[::2]
#print(a)

b = my_list[::-1]
#print(b)

##list comprehension

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [x*2 for x in a if math.sqrt(x) < 2]
#print(b)


#Tuples -> they are immutable bro

new_tuple = ("dayı", )
new_tupke_two = tuple([1, 2, 3, 5])
#print(new_tuple)
#print(new_tupke_two)


#dictionaries

mydict = {"name": "ceren", "age": 28, "city":"Warsaw"}
#print(mydict)

my_dict_two = dict(name="Abudrrahim", age=28, city= "Warsaw")
#print(my_dict_two)

mydict["email"] = "avcrncntn@gmail.com"
#print(mydict)

del mydict["email"]
mydict.pop("age")
#print(mydict)

mydict = {"name": "ceren", "age": 28, "city":"Warsaw"}
#print(mydict)
mydict["email"] = "avcrncntn@gmail.com"
#print(mydict)
""""
for key in mydict.keys():
    #print(key)
for value in mydict.values():
    #print(value)
for key, value in mydict.items():
    #print(key, value)
"""

""""
mydict = {"name": "Abdurrahim", "surname": "Eskin", "age": 28, "city": "Warsaw"}
my_dict_two = dict(name="Ceren", surname="Canatan", occupation="Lawyer", age=28, city="Warsaw")
mydict.update(my_dict_two)
#print(mydict)
"""
### Sets ####
# my_string = "    Hello World     "
# my_string = my_string.strip()
# print(my_string)

# strip -> removes white spaces
# upper/lower -> changes the upper case/ lower case
# startswith/endswith -> returns true or false for the word is existing in the string
# find -> returns the first index of the character in string if exists else it returns -1
# count -> count the numbers of character
# replace -> replaces the input string in the string
# split crates list from a string:

"""
my_string_two = 'Hello,how,was,your,day?'
my_list_two = my_string_two.split(",")
print(my_list_two)
new_string = ' '.join(my_list_two)
print(new_string)
"""


# %, .format(), f-strings
# s-> strings, d-> numbers(decimal), f-> float

var1= 3.141762
my_string1 = "my variable is %f " % var1
print(my_string1)


var2 = 3.141762
var2_1 = 7
my_string2 = "the variable is {:.4f} and {}".format(var2, var2_1)
print(my_string2)

var3 = 4.17261302
var3_1 = 11
my_string3 = f"the variables are {var3:.2f} and {var3_1}"
print(my_string3)

