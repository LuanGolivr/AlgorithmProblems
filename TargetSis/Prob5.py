def reverseStr(value):
    word = []

    for char in value:
        word.append(char)
    
    left = 0
    right = len(word) - 1

    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1
    
    return "".join(word)


s = str(input("Insert a string: "))
print(reverseStr(s))