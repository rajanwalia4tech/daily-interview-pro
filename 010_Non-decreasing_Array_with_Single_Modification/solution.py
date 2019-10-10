def check(lst):
    count = 0 
    for i in range(1, len(lst)):
        if lst[i-1] > lst[i]:
            count += 1
        if count > 1:
            return False
    return True

print (check([13, 4, 7]))
# True
print (check([5,1,3,2,5]))
# False