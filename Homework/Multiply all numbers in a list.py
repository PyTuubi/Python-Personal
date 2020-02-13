def multiply(nums):
    
    x = nums[0]

    for n in nums:
        x *= n
    
    return x


print(multiply([1, 2, 3, -4]))