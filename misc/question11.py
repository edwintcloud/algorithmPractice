# fib finds the nth number in the fibonachi sequence
# this function uses the mathematical formula below
# Fn = {[(√5 + 1)/2] ^ n} / √5
def fib(n):
    phi = (1+5**.5)/2
    return int(round(pow(phi, n)/5**.5))

# test fib function
print("Fib(1):", fib(1))
print("Fib(2):", fib(2))
print("Fib(3):", fib(3))
print("Fib(4):", fib(4))
print("Fib(20):", fib(20))