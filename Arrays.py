"""
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence 
has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a 
smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
"""

def firstDuplicate(a):
    """
    create empty results array
    create match variable = 0
    iterate over a
        if num not in results array
            append to array
        if num in results array 
            set match to num
            return num
    if match == 0
        return -1
    """
    res = set()
    for i in a:
        if i in res:
            return i
        res.add(i)
    return -1

    #Passing all but 2 tests. Failing 2 hidden tests due to runtime
    #results = []
    #match = 0
    #
    #for num in a:
    #    if num not in results:
    #        results.append(num)
    #    elif num in results:
    #        match += num
    #        return num
    #return -1

"""
Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, 
your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the 
triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

"""
def isZigzag(numbers):
    res = []
    n = 3

    for i in range(len(numbers) - n+1):
        if numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2] or numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]:
            res.append(1)
        else:
            res.append(0)

    return res    
