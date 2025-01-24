'''Write a function to replace each alphabet in the given string with another alphabet occurring 
at the n-th position from each of them.'''

def replace_with_nth_position(string, n):
    res = []
    for i in string:
        if i.isalpha():
            start = ord("A") if i.isupper() else ord("a")
            char = chr(start + (ord(i) - start + n) % 26)
            res.append(char)
        else:
            res.append(i)
    return "".join(res)

string = "ABCabc"
n = 2
print(replace_with_nth_position(string, n))