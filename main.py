def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

n = 5
result = calculate_factorial(n)
print(f"Факториал числа {n} равен {result}")
