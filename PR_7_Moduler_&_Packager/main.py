import sys
import os


from modules import datetime_utils, random_utils, uuid_utils, math_utils, file_utils
from package import converter, calculator, module


def main_menu():
    while True:
        print("\n====================================")
        print("    Multi-Utility Toolkit")
        print("====================================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("====================================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            print(f"\nGenerated UUID: {uuid_utils.generate_unique_id()}")
        elif choice == '5':
            file_menu()
        elif choice == '6':
            explore_attributes()
        elif choice == '7':
            print("Thank you for using Multi-Utility Toolkit! Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")

def datetime_menu():
    print("\n--- Datetime and Time Operations ---")
    print("1. Display current date and time")
    print("2. Calculate difference between two dates")
    print("3. Format date into custom format")
    print("4. Countdown Timer")
    ch = input("Enter your choice: ")
    if ch == '1':
        print(f"Current Date and Time: {datetime_utils.get_current_datetime()}")
    elif ch == '2':
        d1 = input("Enter first date (YYYY-MM-DD): ")
        d2 = input("Enter second date (YYYY-MM-DD): ")
        print(datetime_utils.calculate_date_difference(d1, d2))
    elif ch == '3':
        print(f"Custom Date: {datetime_utils.format_custom_date()}")
    elif ch == '4':
        sec = int(input("Enter seconds for countdown: "))
        datetime_utils.start_stopwatch_and_countdown(sec)

def math_menu():
    print("\n--- Mathematical Operations ---")
    print("1. Calculate Factorial")
    print("2. Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes (Circle)")
    ch = input("Enter your choice: ")
    if ch == '1':
        n = int(input("Enter a number: "))
        print(f"Factorial: {math_utils.calculate_factorial(n)}")
    elif ch == '2':
        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest (%): "))
        t = float(input("Enter time (in years): "))
        print(f"Total Compound Amount: {math_utils.calculate_compound_interest(p, r, t)}")
    elif ch == '3':
        deg = float(input("Enter angle in degrees: "))
        func = input("Enter function (sin, cos, tan): ")
        print(f"Result: {math_utils.calculate_trigonometry(deg, func)}")
    elif ch == '4':
        rad = float(input("Enter radius of circle: "))
        print(f"Area: {math_utils.calculate_area_circle(rad)}")

def random_menu():
    print("\n--- Random Data Generation ---")
    print("1. Generate Random Number")
    print("2. Generate Random Password")
    print("3. Generate Random OTP")
    ch = input("Enter your choice: ")
    if ch == '1':
        s = int(input("Enter start range: "))
        e = int(input("Enter end range: "))
        print(f"Random Number: {random_utils.generate_random_number(s, e)}")
    elif ch == '2':
        l = int(input("Enter password length: "))
        print(f"Generated Password: {random_utils.generate_random_password(l)}")
    elif ch == '3':
        print(f"Generated OTP: {random_utils.generate_random_otp()}")

def file_menu():
    print("\n--- File Operations ---")
    print("1. Create/Write a file")
    print("2. Read from a file")
    print("3. Append to a file")
    ch = input("Enter your choice: ")
    filename = input("Enter file name (e.g., data/sample.txt): ")
    if ch == '1':
        txt = input("Enter data to write: ")
        print(file_utils.create_and_write_file(filename, txt))
    elif ch == '2':
        print("\n--- File Content ---")
        print(file_utils.read_file_content(filename))
    elif ch == '3':
        txt = input("Enter data to append: ")
        print(file_utils.append_to_file(filename, txt))

def explore_attributes():
    print("\n--- Explore Module Attributes ---")
    print("Available modules to explore: math_utils, datetime_utils, random_utils")
    mod_name = input("Enter module name to explore: ")
    if mod_name == 'math_utils':
        print(dir(math_utils))
    elif mod_name == 'datetime_utils':
        print(dir(datetime_utils))
    elif mod_name == 'random_utils':
        print(dir(random_utils))
    else:
        print("Module not recognized for local exploration.")

if __name__ == '__main__':
    main_menu()