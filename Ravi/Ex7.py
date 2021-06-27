# 1  

# 2 2  

# 3 3 3  

# 4 4 4 4  

# 5 5 5 5 5
# for i in range(1,6):
#     for column in range(i):
#         print(i,end=" ")
#    print()



# 1 1 1 1 1 

# 2 2 2 2 

# 3 3 3 

# 4 4 

# 5
# for i in range(1,6):
#     for column in range(i,6):
#         print(i,end=" ")
#     print()

# 1 

# 1 2 

# 1 2 3 

# 1 2 3 4 

# 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,(i+1)):
#         print(j,end=" ")
#     print()

# 5 5 5 5 5 

# 4 4 4 4 

# 3 3 3 

# 2 2 

# 1
# for i in range(1,6):
#     for j in  range(i,6):
#         print(6-i,end=" ")
#     print()


# 5 5 5 5 5 

# 5 5 5 5 

# 5 5 5 

# 5 5 

# 5

# for i in range(1,6):
#     for j in  range(i,6):
#         print(5,end=" ")
#     print()


# 1 

# 2 1 

# 3 2 1 

# 4 3 2 1 

# 5 4 3 2 1

# for i in range(1,6):
#     for j in  range(0,i):
#         print(i-j,end=" ")
#     print()


# 0 1 2 3 4 5 

# 0 1 2 3 4 

# 0 1 2 3 

# 0 1 2 

# 0 1
# for row in range(0,5):
#     for column in range(0,(6-row)):
#         print(column,end=" ")
#     print()


# 1 

# 2 3 4 

# 5 6 7 8 9
# a = 1
# for i in range(1,4):
#     for j in range(1,i+i):
#         print(a,end=" ")
#         a+=1
#     print()


# 1

# 3 2

# 6 5 4

# 10 9 8 7
# a = 1
# for i in range(1,5):
#     for j in range(0,i):
#         print(a-j,end = " ")
#     a+=1+i
#     print()

# 1 

# 1 2 1 

# 1 2 3 2 1 

# 1 2 3 4 3 2 1 

# 1 2 3 4 5 4 3 2 1
for i in range(1,6):
    for j in range(1,i+i):
        if j<=i:
            print(j,end=" ")
        else :
            print(j-i,end=" ")
    
    print()