# D = {'Anita': 23, 'Ashwin': 43,
#      'Ahana': '24',
#      'Adarsh': 30, 'Archana': 15}
# try:
#     # iterates through the keys from left to right
#     for key in D:
#         value = D[key]
#         if type(value) == str:
#             raise 'Error'
#         print(f'{key}:{value}')
# except:
#     print("Values cannot be strings")

# L = [1, 3, -1, 4, -2, 5, 3]

# try:
#     n = 10
#     for i in range(n):
#         if L[i] < 0:
#             L[i] = 0
# except IndexError:
#     for i in range(n - len(L)):
#         L.append(0)
# finally:
#     print(L)

try:
    L = [x for x in range(10)]
    f = open('numbers.txt', 'w')
    for x in L:
        f.write(x)
except FileNotFoundError:
    print('File was not found')
except:
    print('This is some other error')
finally:
    print('The file has been closed')
    f.close()