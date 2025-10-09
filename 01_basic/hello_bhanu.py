# print("Bhanu Pratap")


def userName(name, age):
  print(f"my name is {name} and my age is {age}")

chai_one = "lemon tea"
chai_two = "ginger tea"


# ! repr , str, print 
# print(repr(chai_one))
# print(str(chai_two))
# print(chai_one)


# * String
numList = '0123456789'

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


chai = "masala chai"
print('masala' in chai) # true
print('masalaaa' in chai) # false