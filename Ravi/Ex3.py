# Given a string and an integer number n, remove characters from a string starting from zero up to n and
# return a new string
# For example, removeChars("pynative", 4) so 
# output must be tive. Note: n must be less than the length of the string.
def removechar():
    a=input("enter a string= ")
    n=int(input("enter value of n= "))
    if n<len(a):
        print(a[n:])
removechar()