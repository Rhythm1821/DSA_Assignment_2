def findLHS(nums):
    num_count = {}
    longest_subseq = 0

    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    for num in num_count:
        if num + 1 in num_count:
            longest_subseq = max(longest_subseq, num_count[num] + num_count[num + 1])

    return longest_subseq

print(findLHS([1,3,2,2,5,2,3,7]))
