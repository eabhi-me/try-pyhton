def nuMpro(n: int)->int:
    str1 = str(n)
    pro = 1
    for i in str1:
        pro = pro*int(i)
    return pro
# print(nuMpro(123))


def caplize_first_last_char(sentences: str) -> str:
    list_word = sentences.strip().split()
    for i in range(len(list_word)):
        word = list_word[i]
        if len(word) > 1:
            list_word[i] = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            list_word[i] = word.upper()
    return ' '.join(list_word)

# print(caplize_first_last_char("hello word"))


def kth_longest_word(words: list, n :int):
    word_list = sorted(words,key = len,reverse=True)
    return word_list[n-1]
list1 = ["word","hi","non","hello"]
# print(kth_longest_word(list1,2))


def unflatted(t:tuple, n:int, m:int):
    if(len(t)!=m*n):
        print("Not Possible")
        return
    return tuple(t[i*n:(i+1)*n] for i in range(m))

# print(unflatted((1,2,3,4,5,6,7,8,9),3,3))


def most_frequent_element(lst: list) -> int:
    '''
    Arguments:
    lst: list - a list of integers

    Return:
    int - the integer that occurs most frequently, or the largest one
          if there are multiple with the same frequency

    Example:
    >>> most_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    4
    '''
    maxCount = {}
    for i in range(len(lst)):
        element = lst[i]
        if element not in maxCount.keys():
            maxCount[element] = lst.count(element)
            # this is only sorting thr dict based on values
    # maxCount = dict(sorted(maxCount.items(), key= lambda item: item[1], reverse=True)) 
    # return [key for key, value in maxCount.items() if value == max(maxCount.values())]
    max_ferq = max(maxCount,key=lambda x: (maxCount[x],x))
    return max_ferq

print(most_frequent_element([1,1,1,1,1, 2, 2, 3, 3, 3, 4, 4, 4, 4,5,5,5,5,5,5]))
    


def reverse_dict(d):
    return {value: key for key, value in d.items()}

# Reverse the dictionary
my_dict = {1:5,5:8,9:10}
reversed_dict = reverse_dict(my_dict)
# print(reversed_dict)  # Output: {'Alice': 'name', 30: 'age', 'Wonderland': 'city', 'Engineer': 'occupation'}

# Now you can access keys by their original values
# key = reversed_dict.get("Wonderland")
# print(key)  # Output: city
