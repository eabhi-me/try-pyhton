def longest_common_prefix(str1: str) -> str:
    '''Find the longest common prefix among the given words of the sentence. 

    Args:
        sentence (str): A string of space sepearated words.
    Returns: 
        str: longest prefix. 
    '''
    words = str1.split()
    if not words:
        return ""
    
    prefix = words[0]
    for word in words[1:]:
        while word[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix) - 1]
        if not prefix:
            break
            
    return prefix

print(longest_common_prefix("hello hel he"))