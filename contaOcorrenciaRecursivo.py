def count7(N):
    if len(str(N)) == 1 and N == 0:
        return 0
    else:
        if len(str(N)) >= 1:
            if N % 10 == 7:
                return 1 + count7(N/10)
            else:
                return 0 + count7(N/10)


print count7(0), '0'
print count7(7), '1'
print count7(77), '2'
print count7(170), '1'
print count7(1371), '1'
print count7(71556), '1'
print count7(777729), '4'
print count7(5277987), '3'
