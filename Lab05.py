# finding the factorial
num = int(raw_input('please enter a number to find the factorial'))
def factorial(x):
    
    
    pdt = 1
    for i in range(1, x+1):
        pdt = pdt*i
    return pdt
    
print factorial(num)
print ''
# finding the fibonacci series
number = int(raw_input('please enter a number to print the fibonacci series'))
def fibonacci(h):
    list_numbers = []
    r=1
    q=1
    list_numbers.append(q)
    while r <= h:
        list_numbers.append(r)
        r = q+r
        q = r-q
    print list_numbers
fibonacci(number)
print''

# check prime numbers
k = int(raw_input('please enter a number to check if prime'))
def check_Prime(j):
    divisor_count = 0
    
    for i in range(1, j+1):
        if j% i == 0:
            divisor_count = divisor_count +1
    if divisor_count == 2:
        return 'true'
    else:
        return 'false'
print check_Prime(k)     
    
    
