#base,height = map(int,input("enter your base and height").split())
#print(base)
#print(height)
#area = (base*height)/2
#print("area of triangle" + str(area))
# def addtwo(a, b):
#     added = a + b
#     return a
# x = addtwo(2, 7)
# print(x)
list = ['ruchi','rakhi','alok','akash']
def func(list,**kwargs):
    # return [i[:].title() for i in list]
    if kwargs.get("reverse_str") == True:
        return [i[::-1].title() for i in list]
    else:
        return [i.title() for i in list]    
                 
print(func(list,reverse_str = True))