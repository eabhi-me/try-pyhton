def modify_string_1(s: str) -> str:
    even = s[::2]
    odd = s[1::2][::-1] 
    return even+odd

print(modify_string_1("abcdef"))