
"""sumary_line

name = "Abdurrahim"
surname = "Eskin"
value = F"{name} {surname}"
print(value)
"""
import math
#value = "        Mustafam Fatihim ve ben           "
#new_string = "Test String of Find"
#new_test_string = "Mustafam Nabersin"
#new_test_string_two = new_test_string.replace("a", "i")
#print(new_test_string_two)


#print(2**3)
#print(int(math.sqrt(16)))

#test_value = int(input())
#test_value_two = float(input())
#print(test_value)
#print(test_value_two)


#print(27 // 8)
#print(19082 // 13)


#print(round(2.4))
#print(math.ceil(2.2))



#value = input("Please type your name and surname  ")
#new_value = int(value) + 2
#print(f"your name value is: {value}, the sum is {new_value}")

#selection = int(input())
#value = "selection_one" if selection == 1 else "selection_two"
#print(value)


#test_value = int(input())
#value = True if test_value == 1 else False
#other_value = True if value == True else False
#if (value and other_value):
#    print("Your input was 1")
#else: 
#    print("Your input was not 1")


#input = int(input("Enter the last number that you want to go"))
#x=[item for item in range (1, input) if item%2==0]
#print(f" You have {len(x)} even number in the given list", x)


#number=0
#for item in range (1,10):
#    if item%2==0:
#        print(item)
#        number += 1

#print(f" we have {number} even numbers in the given range")




#letters=["a", "b", "c", "d"]
#for letter in enumerate(letters):
#    print(letter[1])

#new_list=list(range(20))
#new_list.insert(0,"20")
#print(new_list)


#new_list=[
#    ("item1", 5),
#    ("item2", 4),
#    ("item3", 3),
#    ("item4", 2)
#]
#test=[]
#for product, price in new_list:
#        test.append(price)
#print(test)



#my_list=list(range(100))

#new_list=[item for item in my_list if item%2== 0 ]
#print(new_list)

#test_set={'Dayi', "AloFatih", 2, 7, 9, 9, 10}
#print(test_set)


#my_dict = {"valuOne":"Fatihim", "valuTwo":"Mustafam", "valuThree":"adamdeğilsin"}

#for key, value in my_dict.items():
#    print(key, value)


class Human:
    def __init__(self, age, height, weight, skin_color, religion, list_of_companies) -> None:
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__skin_color = skin_color
        self.__religion = religion
        self.__list_of_companies = list(list_of_companies)

    def print_attiributes(self):
        print(self.age, self.height, self.religion, self.skin_color, self.weight, self.list_of_companies)


if __name__ == "__main__":
    abdurrahim = Human(29, 184, 84, "Dark_white", "Islam", ["IBM", "Sabanci", "Fiba"])
    print(abdurrahim.__dict__)
    a = (1,5,7,9,3)
    print(a)
    a[3]=2
    print(a)