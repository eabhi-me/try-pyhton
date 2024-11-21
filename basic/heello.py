# def unique(L):
#     L_uniq = [ ]
#     for i in range(0, len(L)):
#         if not(L[i] in L[i + 1: ]):
#             L_uniq.append(L[i])
#     return L_uniq
# x = unique([1, 1, 2, 3, 5, 5])
# for i in x:
#   print(i)


# A method to use the offer
# total_price = 0
# while True: # repeat forever since we are breaking inside
#     line = input().lower()
#     if line == "end": # The terminal condition
#         break
#     quantity, price = line.split() # split uses space by default
#     quantity, price = int(quantity), int(price) # convert to ints
#     total_price += quantity * price # accumulate the total price
# print(total_price)


# method format
# value = []
# while True:
#     line = input()
#     if line.lower() == "stop":
#         break
#     if line.lower().endswith("ed") or line.lower().endswith("ing"):
#         value.append(line)
# print(value)


# all value that revese sum is palindrome
# for num in range(1000):
#     if num == -1:
#         break
#     reverse_num = int(str(num)[::-1])
#     total = num + reverse_num
#     if(str(total) == str(total)[::-1]):
#         print(num)


# line = input()
# while line != "":
#     print(2*line)
#     line = input()
# print(line)

# result = []
# while True:
#     line = input()
#     if line.endswith("."):
#         result.append(line[::2])
#         break
#     else:
#         result.append(line[::2])
# print(" ".join(result))


# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     for j in range(i-1, 0, -1):
#         print(j, end='')
#     print()


# n = int(input())
# if (n > 0):
#     for i in range(1, n + 1):
#         if (n % i == 0):
#             print(i)



# direction = input()
# x_distance, y_distance = 0, 0
# while (direction != 'STOP'):
#     if (direction =='LEFT'):
#         x_distance -= 1
#     elif (direction == 'RIGHT'):
#         x_distance += 1
#     elif (direction == 'UP'):
#         y_distance += 1
#     elif (direction == 'DOWN'):
#         y_distance -= 1
#     x, y = abs(x_distance - 0), abs(y_distance - 0)
#     manhattan_distance = x + y
#     direction = input()
# print(manhattan_distance)

pangram = 'the quick brown fox jumps over the lazy dog'
words = pangram.split(' ')          # get list of words in the sentence
letters = ''.join(words)            # join the words back; eliminates spaces
sorted_letters = sorted(letters)    # sort letters
mapping, count = dict(), 0
for letter in sorted_letters:
    # check if letter is not present in dict
    # to avoid counting same letter multiple times
    if letter not in mapping:
        count += 1
        mapping[letter] = count     # map the letter to count

for letter, count in mapping.items():
    print(letter, count)
