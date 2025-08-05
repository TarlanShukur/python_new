# This is an advanced module file

def factorial_calculate(n):
    """Calculates the factorial of a given number"""

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_calculate(n-1)
    


def fibonacci_series(n):
    """Generates a fibonacci series for a given number of times"""
        
    fibonacci_list = [0, 1]
        
    while len(fibonacci_list) < n:
        new_element = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(new_element)

    return fibonacci_list    

def square_root(number):
    """Calculates the square root of a given number."""

    if number < 0:
        return "Negative numbers no square root"
    
    else:
        return number ** 0.5

# print(factorial_calculate(int(input("Faktoriyeli alinacak sayi:"))))

# print(fibonacci_series(int(input("Fibonacci degeri icin bir sayi girin"))))

# print(square_root(int(input("Karekokini alinasi istediginiz sayiyi girin"))))
