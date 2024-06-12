# name1 = "hello";
# name2 = "gello";
# print(name1>name2);

# print(input() < input())
# x = 2 ** 5
# print(x)
# x1 = x // 2
# print(x1)
# x2 = x1 // 2
# print(x2)
# x3 = x2 // 2
# x4 = x3 // 2
# x5 = x4 // 2
# print(x1 + x2 + x3 + x4 + x5)
# print(16+8+4+2+1)

# print(abs(9-45))
# output4 = abs((4+5)-(4*5))
# print(output4)

# Sample inputs (# note: This prefix code (grey) won't be run by the auto grader)
# a = 5
# b = 6
# price, discount_percent = 80, 5.75
# total_mins = 470
# <eoi>

# output1 = a+b # int: sum of a and b
# output2 = 2*(a+b) # int: twice the sum of a and b
# output3 = abs(a-b) # int: absolute difference between a and b
# output4 = abs((a+b)-(a*b)) # int: absolute difference between sum and product of a and b

# # Find discounted price given price and discount_percent
# # input variables : price: int, discount_percent: float
# discounted_price = (price)-(price*discount_percent)/100 # float

# # Round the discounted_price
# rounded_discounted_price = discounted_price # int

# # Find hrs and mins given the total_mins
# # input variables : total_mins
# hrs = total_mins//60 # int: hint: think about floor division operator
# mins = total_mins%60 # int
# print(output1,output2,output3,output4,discounted_price,rounded_discounted_price)

# Sample inputs (# note: This prefix code (grey) won't be run by the auto grader)
a = 5

price1, discount1 = 50, 4 # for offer1
price2, discount2 = 60, 8 # for offer2

# Assume discount is given in percentages

# <eoi>

output1 = a>5 # bool: True if a greater than or equal to 5

# output2 = a%5==0 # bool: True if a is divisible by 5

# output3 = a%2!=0 and a<10 # bool: True if a is odd number less than 10

# output4 = a%2!=0 and a<10 and a>-10 # bool: True if a is an odd number within the range -10 and 10

# output5 = 0 # bool: True if a has even number of digits but not more than 10 digits
# while(a>0):
#     output5 = output5+1
#     a//10


# is_offer1_cheaper = (price1-discount1*price1/100)-(price2-discount2*price2/100) # bool: True if the offer1 is strictly cheaper
print(output1)
# print(output1,output2,output3,output4,output5,is_offer1_cheaper)
