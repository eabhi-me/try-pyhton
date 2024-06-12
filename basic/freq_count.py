num = int(input("enter the number of list num: "))    # declare a variable
lst =[]  # a list to store the number
for i in range(num):  # loop to take the input 
    n = int(input("enter the number: "))
    lst.append(n)  # adding the number to list
srnum = int(input("enter the number to search: "))
ncount = 0
for n in lst:
    if n == srnum:
        ncount=ncount+1
print(ncount)
