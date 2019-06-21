def maxSubArraySum(a):

    max_so_far =a[0]
    curr_max = a[0]

    for i in range(1,len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)

    return max_so_far

result = maxSubArraySum([1,2,3,-1, -11,11])
print(result)
