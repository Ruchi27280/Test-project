list = ['ruchi','rakhi','alok','akash']
def func(list,**kwargs):
    # return [i[:].title() for i in list]
    if kwargs.get("reverse_str") == True:
        return [i[::-1].title() for i in list]
    else:
        return [i.title() for i in list]    
                 
print(func(list,reverse_str = True))
print("ruchi")
print("alok")
print("akash")
print("rakhi")