# triplets = [ ]
# for x in range(1, 100):
#     for y in range(x + 1, 100):
#         for z in range(y + 1, 100):
#             if x ** 2 + y ** 2 == z ** 2:
#                 triplets.append((x, y, z))
# for res in triplets:
#     print(res)

# triplets = [(x, y, z) for x in range(1, 100) 
#             		  for y in range(1, 100)
#            			  for z in range(1, 100)
#            			  if x ** 2 + y ** 2 == z ** 2 and x < y < z]
# for res in triplets:
#     print(res)

# triplets = [(x, y, z) for x in range(1, 100) 
#             		  for y in range(x + 1, 100)
#            			  for z in range(y + 1, 100)
#            			  if x ** 2 + y ** 2 == z ** 2]
# for res in triplets:
#     print(res)

# L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
# for i in L:
#     print(i)
# print("/n/n/n")
# L = [ ]
# for x in [1, 2, 3]:
#     for y in [3, 4, 5]:
#         if y > x:
#             L.append(y - x)
# for i in L:
#     print(i)

# print([word for word in input().split(',') if 'e' not in word])

L = [90, 47, 8, 18, 10, 7]
S = [L[0]]	# list containing just one element
for i in range(1, len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j = S[: j]	# elements in S before index j
            new_j = [L[i]]		# list containing just one element
            after_j = S[j: ]	# elements in S starting from index j
            # what is the size of S now?
            S = before_j + new_j + after_j
            # what is the size of S now?
            flag = False
            break
    if flag:
        S.append(L[i])
print(S)