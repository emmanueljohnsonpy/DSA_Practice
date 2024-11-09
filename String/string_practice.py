

# Replace each alphabet in the given string with another alphabet occurring at the n-th position from each of them

n=3
string="abcdefg"

def converting_str(n, string):
    res=""
    for char in string:
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            new_char=chr(start + (ord(char)-start+n)%26)
            res+=new_char
        else:
            res+=char
    return res

result=converting_str(n, string)
print(result)


# Write a function that checks whether two given strings are anagrams of each other. 
# Two strings are anagrams if they contain the same characters in the same frequency, 
# but possibly in a different order.
from collections import Counter

str1="listen" 
str2="silent"
str3="hello" 
str4="world"

def check_anagram(str1, str2):
    return Counter(str1)==Counter(str2)

print(check_anagram(str1, str2))

