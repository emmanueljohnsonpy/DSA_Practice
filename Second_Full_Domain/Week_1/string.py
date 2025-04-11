test1 = "abcd"
test2 = "xyz"
k = 5

def string_shifting(test1, k):
    res = ""
    for char in test1:
        if char.isalpha():
            if char.isupper():
                c = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            else:
                c = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            res += c
        else:
            res += char
    return res
    
print(string_shifting(test1, k))
print(string_shifting(test2, k))