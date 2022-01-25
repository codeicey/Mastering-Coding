cube = lambda x: pow(x,3)# complete the lambda function 0,1,1,2,3

def fibonacci(n):
    a, b = 0,1
    list1 = []
    for x in range(n):
        list1.append(cube(a))
        fib = a + b
        # update values
        a = b
        b = fib
    return list1
 
print(fibonacci(int(input())))
    
