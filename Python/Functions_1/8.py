def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

print(contains_007([1, 2, 0, 0, 7, 8]))    # Output: True
print(contains_007([1, 0, 0, 7, 2, 3]))    # Output: True
print(contains_007([1, 2, 3, 4, 0, 0, 7])) # Output: True
print(contains_007([1, 2, 0, 7, 8, 0]))    # Output: False