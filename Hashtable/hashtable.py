

# Accessing 


my_dict={'Dave': '001', 'Ava': '002', 'Joe': '003'}
print(my_dict)
print(my_dict['Dave'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Ava'))
print('------------------------------')
for x in my_dict:
    print(x)
print('------------------------------')
for x in my_dict.values():
    print(x)
print('------------------------------')
for x, y in my_dict.items():
    print(x, y)
print('------------------------------')


# Updating


my_dict={'Dave': '001', 'Ava': '002', 'Joe': '003'}
my_dict['Dave']='003'
my_dict['Charles']='004'
print(my_dict)


# Deleting


my_dict={'Dave': '001', 'Ava': '002', 'Joe': '003'}
my_dict.pop('Ava')
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict['Dave']
print(my_dict)


a={'1': 'yo', '1': 'yoyo'}
print(a['1']) 

def first_non_repeating_char(s):
    my_dict={}
    for i in range(len(s)):
        if s[i] in my_dict:
            my_dict[s[i]]+=1
        else:
            my_dict[s[i]]=1
    for i, v in enumerate(s):
        if my_dict[v]==1:
            return i
    return -1

s='loveleetcode'
print(first_non_repeating_char(s)) 




def two_sum(arr, target):
    my_dict={}
    for i, v in enumerate(arr):
        diff=target-v
        if diff in my_dict:
            return [my_dict[diff], i]
        my_dict[v]=i
    return -1




print(two_sum([2, 7, 11, 15], 9))   
print(two_sum([3, 2, 4], 6))   


from collections import defaultdict

def group_anagrams(arr):
    my_dict=defaultdict(list)
    for i in arr:
        s=tuple(sorted(i))
        my_dict[s].append(i)
    return list(my_dict.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))













        








































































