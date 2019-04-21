def ns(n):
    if n <= 1:
        return 1
    else:
        return ns(n-1)*n

print('XLL')
print(ns(5))
print(ns(3))

