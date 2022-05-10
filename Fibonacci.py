def FIB(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    fib_array = [0, 1, 1]
     
    for i in range(3, n+1):
        num = fib_array[i-1] + fib_array[i-2]
        fib_array.append(num)
        
    return fib_array[n]

print(FIB(35))

