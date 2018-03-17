def fib2(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f1 + f0
        yield f1
        
        
print(*fib2(100))
