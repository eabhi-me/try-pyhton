def count_values_occurrences(d):
    dictn = {}
    for val in d.values():
        if val not in dictn.keys():
            dictn(val) = 1
        elif val in dictn.keys():
            dictn(val)=dictn(val)+1
    return dictn
dict1 = {"1":5,"2":5,"10":1}
print(count_values_occurrences(dict1))