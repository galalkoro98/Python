# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still unproven)
# which can be described in the following way:
#  1. take any none-negative and non-zero integer number and named c0:
#  2. if it's even, evaluate a new c0 as c0 / 2;
#  3. otherwise (if it's odd), evaluate a new c0 as c0 * 3 + 1;
#  4. if c0 !=, go back to point 2. 

#  The hypothesis says that regardless of initial value of c0 as c0 * c0 + 1.

c0 = int(input("Enter an integer number: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    steps += 1
    print("Step", steps, "- Current value of c0:", c0)

print("Final value of c0 is 1. Collatz Conjecture holds in", steps, "steps!")


