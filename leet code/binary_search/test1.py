def binary_search(l, i):
    low = 0
    high = len(l) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        steps+=1
        if guess == i:
            print(steps)
            return mid
        
        elif guess > i:
            high = mid - 1
        
        else:
            low = mid + 1
    return None

print(binary_search([i for i in range(1, 101)], 52))