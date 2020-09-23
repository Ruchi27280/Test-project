# Given a string and an integer number n, remove characters from a string starting from zero up to n and
# return a new string
# For example, removeChars("pynative", 4) so 
# output must be tive. Note: n must be less than the length of the string.
string = input("enter any string")
num = int(input("enter a number"))
if num < len(string):
    print(string[num:])
else:
    print("give no. which is less than length of string")
# def func(string,num):
#     if num < len(string):
#         return string[num:]
#     else:
#         return "wrong input"
# print(func(string,num))

