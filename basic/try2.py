# Sample inputs (# note: This prefix code (grey) won't be run by the auto grader)
a = 5

price1, discount1 = 50, 4 # for offer1
price2, discount2 = 60, 8 # for offer2

# Assume discount is given in percentages

# <eoi>

output1 = a>5 # bool: True if a greater than or equal to 5

output2 = a%5==0 # bool: True if a is divisible by 5

output3 = a%2!=0 and a<10 # bool: True if a is odd number less than 10

output4 = a%2!=0 and -10 < a < 10 # bool: True if a is an odd number within the range -10 and 10

output5 = len(str(a)) % 2 == 0 and len(str(a)) <= 10 # bool: True if a has even number of digits but not more than 10 digits
is_offer1_cheaper = price1*(1-discount1/100)<price2*(1-discount2/100) # bool: True if the offer1 is strictly cheaper
print(output1,output2,output3,output4,output5)

string = "example"
every_second_character = string[1::2]
print(every_second_character)

reversed_string = string[::-1]
print(reversed_string)




last_three_elements = string[-3:]
print(last_three_elements)

ends_with_a = word1.endswith('a') or word1.endswith('A')

word1 = "hello"
word2 = "world"
word3 = "example"
n1 = 123

new_word = word1[:4] + "-" + word2[-4:]
new_word2 = word3 + " " + str(n1)
print(new_word)
print(new_word2)

hyphen = "-" * 50
print(hyphen)

