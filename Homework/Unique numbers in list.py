def unique_list(nums):
    
    uniqueList = []

    for n in nums:
        if n not in uniqueList:
            uniqueList.append(n)

    return uniqueList



print(unique_list([1,1,1,2,2,2,3,3,4,4,5,5,6,7,7,7,8,9,9]))