def longestRun(L):
    c_list = []
    f_list = []
    if len(L) == 0:
        return len(f_list)
    if len(L) == 1:
        return len(L)
    for i in range(len(L)):
        if i < len(L) - 1:
            #if L[i] <= L[i + 1]:
            if L[i + 1] >= L[i]:
                c_list.append(L[i])
            else:
                c_list.append(L[i])
                if len(f_list) < len(c_list):
                    f_list = c_list[:]
                c_list = []
        else:
            if L[-1] >= L[-2]:
                c_list.append(L[-1])
                if len(f_list) < len(c_list):
                    f_list = c_list[:]
    return f_list, len(f_list)
        
    
print longestRun([10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9]),'6'
print longestRun([1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0]),'5'
print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2]),'5'
print longestRun([1, 1, 1, 1, 1]),'5'
print longestRun([-10, -5, 0, 5, 10]),'5'
print longestRun([-1, -2, -3, -4, -5, -6, -7, 2, 3]),'3'
print longestRun([1, 3, 5, -1, -3, -5, -7, 1, 3, 5]),'4'
print longestRun([10, 8, 9, 5, 6, 7, 1, 2, 3, 4]),'4'
