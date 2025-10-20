# print("Bhanu Pratap")


# def userName(name, age):
#     print(f"my name is {name} and my age is {age}")


# chai_one = "lemon tea"
# chai_two = "ginger tea"


# ! repr , str, print
# print(repr(chai_one))
# print(str(chai_two))
# print(chai_one)


# * String
numList = "0123456789"

# print(numList[:])
# print(numList[3:])
# print(numList[3:6])
# print(numList[0:7:2])
# print(numList[0:7:3])
# print(numList[0:7:4])


chai = "masala_chai"
# print(chai.upper())


newChai = "     ginger chai  "

# print(newChai.strip()) # ginger chai

# chai = "lemon chai"
# print(chai.replace("lemon", 'ghar ki'))

# chai  = 'lemon, ginger, masala, mint'
# print(chai.split(" , "))

# chai = "masala Chai"
# print(chai.find('chai'))  #-1
# print(chai.find('Chai'))  #-1


# chai = "ginger chai chai chai"
# print(chai.count("chai"))  #3


# chai_type = "lemon"
# quantity = 2

# order = 'i ordered {} tea with the quantity of {}'

# print(order.format(chai_type, quantity))


# # //! Converting a String to a List
# my_string = "apple,banana,cherry"
# my_list = my_string.split(',')
# print(my_list) # Output: ['apple', 'banana', 'cherry']


# # //* Using list() for individual characters.
# my_string = "hello"
# my_list = list(my_string)
# print(my_list)     # Output: ['h', 'e', 'l', 'l', 'o']

# # //! Converting a List to a String
# my_list = ['apple', 'banana', 'cherry']
# my_string = ','.join(my_list)
# print(my_string)    # Output: apple,banana,cherry

# # //* Using map() with str() and join() for mixed-type lists:
# my_list = [1, 'apple', 3.14, 'banana']
# my_string = ' '.join(map(str, my_list))
# print(my_string) # Output: 1 apple 3.14 banana

# chai = "ginger tea"
# for letter in chai:
#     print(letter, end=' ', flush=True)  # print with a space
#     # print(letter, flush=False)  # print without a space

# //! raw string
# newData = "bhanu\anurag"
# print(newData)
# data = r"bhanu\anurag"
# print(data)

# drive  = r"c:\user\pwd"
# drive  = "c:\user\pwd"
# solution of above line without raw
# drive1 = "c:\\user\\pwd" # correct
# print(drive1)


# chai = "masala chai"
# print('masala' in chai) # true
# print('masalaaa' in chai) # false


# //! List or Array

# a = [1, 2, 3, 4, 5]
# b = ["apple", "banana", "cherry"]
# c = [1, "hello", 3.14, True]

# print(a)
# print(b)
# print(c)


# a = list((1, 2, 3, "apple", 4.5))
# print(a)
# b = list("GFG")
# print(b)


# a = [2] * 5
# b = [0] * 7

# print(a)
# print(b)


# a = [10, 20, 30, 40, 50]
# print(a[0])
# print(a[-1])
# print(a[1:4])   # elements from index 1 to 3


# //* Adding Elements into List [append, extend, insert, clear]

# a = []
# a.append(10)
# print("After append(10):", a)

# a.insert(0, 5)
# print("After insert(0, 5):", a)

# a.extend([15, 20, 25])
# print("After extend([15, 20, 25]):", a)

# a.clear()
# print("After clear():", a)

# //? Updating Elements into List
# a = [10, 20, 30, 40, 50]
# a[1] = 25
# print(a)


# //? Removing Elements into List [remove , pop, del]


# a = [10, 20, 30, 40, 50]

# a.remove(30)
# print("After remove(30):", a)

# popped_val = a.pop(1)
# print("Popped element:", popped_val)
# print("After pop(1):", a)

# del a[0]
# print("After del a[0]:", a)

# print(a)


# //? Iterating Over Lists

# a = ['apple', 'banana', 'cherry']
# for item in a:
#     print(item)

# //? Nested Lists
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][2])


# //? List Comprehension
# //* List comprehension is a concise way to create lists using a single line of code. It is useful for applying an operation or filter to items in an iterable, such as a list or range.

# squares = [x**2 for x in range(1, 6)]
# print(squares)

""" 
Explanation:

for x in range(1, 6): loops through each number from 1 to 5 (excluding 6).
x**2: squares each number x.
[ ]: collects all the squared numbers into a new list.
"""


#! Dictionary

chai_types = {"masala": "spicy", "Ginger": "Zesty", "Green": "mild"}
# print(chai_types)
# print(chai_types["masala"])
# print(chai_types.get("Green"))
# chai_types["Green"] = "Fresh"
# print(chai_types['Green'])

# for chai in chai_types:
#    print(chai)


# for chai in chai_types:
#    print(chai, chai_types[chai])

# for key, value in chai_types.items():
#    print(key, value)

# if "Ginger" in chai_types:
#     print("Yes we have Ginger tea")
# else:
#     print("No , we dont have")


# print(len(chai_types))

# chai_types["Earl Grey"] = "Citrus"
# print(chai_types)

# popped_item = chai_types.pop("Ginger")
# print("Popped item:", popped_item)

# popped_item = chai_types.popitem()
# print("Popped item:", popped_item)

# #? Dictionary inside Dictionary example
# example_dict = {
#     "name": "John Doe",
#     "age": 25,
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "state": "NY"
#     }
# }
# print(example_dict["address"]["city"])


# squared_num = {x:x**2 for x in range(10)}
# print(squared_num)
# squared_num.clear()
# print(squared_num)
