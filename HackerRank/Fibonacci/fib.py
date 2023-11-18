""" Fibonacci Sequence - Basic Coding Example

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    F(4) = F(3) [1] + F(2) [1] = 2
    F(5) = F(4) [2] + F(3) [1] = 3
    
    Fn = F(n-1) + F(n-2)
"""

""" Naive solution
    Slow
    
    F(20) = F(19) + F(18)
            [F(18) + F(17)] + [F(17) + F(16)]
"""
def fib(n):
    if n < 0:
        print("Invalid num, can only positive numbers")
        return -1
        
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    return fib(n-1) + fib(n-2)
    
    
"""
    Faster
    Build up 
    But we compute every time, not ideal
"""
def build_fib(n):
    if n < 0:
        print("Invalid num, can only positive numbers")
        return -1
        
    fib_nums = [0, 1]
    
    for i in range(2,n+1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
         
    return fib_nums[n]
    
"""
    Memoization - Compute an expensive function once,
    save the values for other times
"""
def mem_fib(n, fib_nums={0:0, 1:1}):
    if n < 0:
        print("Invalid num, can only positive numbers")
        return -1

    if n not in fib_nums:
        fib_nums[n] = mem_fib(n-1) + mem_fib(n-2)
        
    print(fib_nums)
    return fib_nums[n]

"""
    build_fib with memoization
"""
def mem_improved(n, fib_nums={0:0, 1:1}):
    if n < 0:
        print("Invalid num, can only positive numbers")
        return -1
    
    for i in range(2,n+1):
        fib_nums[i] = (fib_nums[i-1] + fib_nums[i-2])
    
    #print(fib_nums)
    return fib_nums[n]

def main():
    print("Input number to calculate in the fibonacci sequence")
    x = input()
    n = int(x)
    
    # output 1
    # print("naive fib")
    # print(fib(n))
    # fib_nums = [fib(i) for i in range(n+1)]
    # print(fib_nums)
    # print()
    
    #output 2
    # print("build fib")
    #print(build_fib(n))
    # print(build_fib(n-1))
    # print(build_fib(n-2))
    
    #output 3
    # print("mem fib")
    # print(mem_fib(n))
    # print("n-1")
    # print(mem_fib(n-1))
    # print("n-2")
    # print(mem_fib(n-2))
    # print("n+1")
    # print(mem_fib(n+1))
    
    #output 4
    # print("improved mem fib")
    print(mem_improved(n))
    # print("n-1")
    # print(mem_improved(n-1))
    # print("n-2")
    # print(mem_improved(n-2))
    # print("n+1")
    # print(mem_improved(n+1))
    
if __name__ == "__main__":
    main()