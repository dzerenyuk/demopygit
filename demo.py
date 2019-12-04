#print('Hello world')
#print('Adding new line')
#print('I won\'t stop in Python learning ')


def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum
print(factorial(6))