

# Find the target element in an array and return its index


arr = [3, 5, 2, 9, 4]
target = 9
def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(find_index(arr, target)) 


# Return all indices where the target element occurs


arr = [1, 4, 2, 4, 5, 4]
target = 4
def indeces_of_element(target, arr):
    res=[]
    for i in range(len(arr)):
        if arr[i]==target:
            res.append(i)
    return res if res else -1

print(indeces_of_element(target, arr)) 


# Find the index of a target character in a string


string = "interview"
target = 'v'
def find_index(string, target):
    for i in range(len(string)):
        if string[i]==target:
            return i
    return -1
print(find_index(string, target)) 


# Find the coordinates of a target element in a 2D array


matrix = [[1, 2], [3, 4], [5, 6]]
target = 4
#Output: (1, 1)
def find_cordinates(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==target:
                return (i, j)
    return -1
print(find_cordinates(matrix, target)) 


# Find the minimum or maximum element in an array


arr = [5, 3, 8, 6, 2]
def find_min(arr):
    min=arr[0]
    for i in range(1, len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min
print(find_min(arr)) 


# Find the element closest to the target value in an array


arr = [7, 4, 9, 10, 3]
target = 8
# Output: 7
def find_closest(arr, target):
    closest=arr[0]
    for i in range(len(arr)):
        if abs(arr[i]-target)<abs(closest-target):
            closest=arr[i]
    return closest
print(find_closest(arr, target))