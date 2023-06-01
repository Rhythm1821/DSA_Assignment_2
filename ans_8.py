def minimumScore(nums, k):
    min_score = float('inf')
    max_score = float('-inf')

    for i in range(len(nums)):
        # Update the minimum and maximum values
        min_score = min(min_score, nums[i])
        max_score = max(max_score, nums[i])

    # Check all possible values of x and update the minimum score
    for i in range(len(nums)):
        for x in range(-k, k+1):
            new_min = min_score + x
            new_max = max_score + x
            min_score = min(min_score, new_max - new_min)

    return min_score
print(minimumScore([1],0))