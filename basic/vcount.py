myVar = input()
vowels = "aeiouAEIOU"
vCount = 0
for char in myVar:
    if char in vowels:
        vCount = vCount+1 
print(vCount)