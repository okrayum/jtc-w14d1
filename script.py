# W14D1 After Class Assignment
import random

# Merge Sort Function
def merge_sort(nums):
  if len(nums) <= 1: # O(1)
    return nums # O(1)
  
  # Divide the nums array into two halves
  mid = len(nums) // 2 # O(1)
  left = nums[:mid] # O(n)
  right = nums[mid:] # O(n)

  # Sorth both halves recursively
  left = merge_sort(left) # T(n/2)
  right = merge_sort(right) # T(n/2)

  # Merge the soreted halves
  return merge(left, right) # O(n)

# Merge Helper Function
def merge(left, right): # O(1)
  result = [] # O(1)
  left_i = 0 # O(1)
  right_i = 0 # O(1)

  while left_i < len(left) and right_i < len(right): # O(n)
    if left[left_i] < right[right_i]: # O(1)
      result.append(left[left_i]) # O(1)
      left_i += 1 # O(1)
    else:
      result.append(right[right_i]) # O(1)
      right_i += 1 # O(1)

  # Append any remaining elements form left or right subarrays
  result.extend(left[left_i:]) # O(n)
  result.extend(right[right_i:]) # O(n)

  return result # O(1)
# overall bigO = O(n log n) 

# Test cases
print(merge_sort([5, 2, 3, 1]))  # Example 1
print(merge_sort([5, 1, 1, 2, 0, 0]))  # Example 2
print(merge_sort([]))  # Edge case: empty array
print(merge_sort([1]))  # Edge case: array with one element
print(merge_sort([5, 4, 3, 2, 1]))  # Array sorted in descending order
print(merge_sort([1, 2, 3, 4, 5]))  # Array already sorted
print(merge_sort([-5, -2, -3, -1]))  # Array with negative numbers
print(merge_sort([5, -2, 0, 3, -1]))  # Array with both positive and negative numbers
# Test cases with larger arrays
print(merge_sort([random.randint(-50000, 50000) for _ in range(1000)]))  # Array with 1000 random elements




