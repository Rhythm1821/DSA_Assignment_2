def maxCandies(candyType):
    uniqueTypes = set()
    for candy in candyType:
        uniqueTypes.add(candy)
        if len(uniqueTypes) == len(candyType) // 2:
            break
    return min(len(uniqueTypes), len(candyType) // 2)
print(maxCandies( [1,1,2,2,3,3]))

