import math


def calculate_factorial(n):
     return math.factorial(n)
def calculate_compound_interest(principal, rate, time_years):
    # Formula: A = P * (1 + R/100)^T
    amount = principal * math.pow((1 + rate / 100), time_years)
    return round(amount, 2)

def calculate_trigonometry(angle_degrees, func_name):
    radians = math.radians(angle_degrees)
    if func_name.lower() == 'sin':
        return round(math.sin(radians), 4)
    elif func_name.lower() == 'cos':
        return round(math.cos(radians), 4)
    elif func_name.lower() == 'tan':
        return round(math.tan(radians), 4)
    return "Invalid Function"

def calculate_area_circle(radius):
    return round(math.pi * math.pow(radius, 2), 2)