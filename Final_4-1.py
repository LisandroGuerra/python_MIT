def getSublists(L, n):
    new = []
    if len(L) == 1:
        return [L]
    if n == 1:
        return [[e] for e in L]
    for i in range(len(L[:-(n-1)])):
        new.append(L[i:i+n])

    return new
        
    


print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 4)
print 'R:[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]'
print '---------------------------------------'
print getSublists([1, 1, 1, 1, 4], 2)
print 'R:[[1, 1], [1, 1], [1, 1], [1, 4]]'
