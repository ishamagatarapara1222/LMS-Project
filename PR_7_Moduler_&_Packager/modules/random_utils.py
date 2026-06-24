import random
import string

def generate_random_number(start, end):
    return random.randint(start, end)

def generate_random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def generate_random_otp():
    return "".join(random.choice(string.digits) for _ in range(6))