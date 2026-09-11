from numpy import inf


arr = [10,20,30,40]
for value in arr:
    print(value)

for i in range(len(arr)):
    print(i, arr[i])

"""O(1)   → Jump
O(n)   → Walk
O(n²)  → Everyone meets everyone
Therefore, o(1) is fastest and o(n²) is slowest. The time complexity of an algorithm is a measure of the amount of time it takes to run as a function of the length of the input.
 It helps us understand how the algorithm scales with larger inputs."""

# ARRAY PROBLEM
# Need to check every element? -> Traversal
# Need to find/count something? -> Traversal / Hashing
# Need a pair of elements? -> Two Pointers / Hashing
# Continuous subarray/window? -> Sliding Window
# Sorted array + searching? -> Binary Search
# Find the largest number in the list[3,7,9,5]? -> Traversal

arr = [3, 5, 9, 5]


def find_max(arr):
    max_val = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


print(find_max(arr))  # Output: 9

#Find the second largest number in the list[10,5,8,20,15]? -> Traversal
arr = [10, 5, 8, 20, 15]
def find_second_largest(arr):
    second_largest = float('-inf')
    first_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > first_largest:
            second_largest = first_largest
            first_largest = arr[i]
        elif arr[i] > second_largest and arr[i] != first_largest:
            second_largest = arr[i]
    return second_largest

print(find_second_largest(arr))  # Output: 15