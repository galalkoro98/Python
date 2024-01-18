# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     product = 1
#     for i in range (2, n + 1):
#         product = product * i
#     return product

# for n in range(1, 6):
#     print(n, factorial_function(n))



# def fib(n):
#     if n < 0:
#         return None
#     if n < 3:
#         return 1
#     elm_1 = elm_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elm_1 + elm_2
#         elm_1, elm_2 = elm_2, the_sum
#     return the_sum

# for n in range(1, 10):
#     print(n, "->", fib(n))


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(100))

def factorial(n):
    if n == 1:
        return 1
    else:
       return n * factorial(n - 1)


print(factorial(5))

