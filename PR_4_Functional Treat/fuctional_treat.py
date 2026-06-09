"""
PROJECT: Functional Treat
Data Analyzer and Transformer Program

Features:
 Menu Driven Interface
 1D and 2D Arrays
 Built-in Functions
 User Defined Functions (UDF)
 *args, **kwargs, __doc__
 Recursion (Factorial & Fibonacci)
 Lambda Functions
 Global Keyword
 Return Multiple Values
 Sorting
"""

# Global Variables
data_1d = []
data_2d = []
summary = {}


# ------------------------------
# Data Input Functions
# ------------------------------
def input_1d():
    """Input a 1D array."""
    global data_1d
    data_1d = list(map(int, input("Enter numbers separated by space: ").split()))
    print("1D Array Stored Successfully!")


def input_2d():
    """Input a 2D array."""
    global data_2d

    rows = int(input("Enter number of rows: "))
    data_2d = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        data_2d.append(row)

    print("2D Array Stored Successfully!")


# ------------------------------
# Built-in Functions
# ------------------------------
def display_summary():
    """Display summary using built-in functions."""

    if not data_1d:
        print("No Data Available!")
        return

    print("\n----- DATA SUMMARY -----")
    print("Total Elements :", len(data_1d))
    print("Minimum Value  :", min(data_1d))
    print("Maximum Value  :", max(data_1d))
    print("Sum            :", sum(data_1d))
    print("Average        :", round(sum(data_1d) / len(data_1d), 2))


# ------------------------------
# User Defined Functions
# ------------------------------
def calculate_average(*args):
    """Returns average using *args."""
    return sum(args) / len(args)


def show_description(**kwargs):
    """Display dataset description using **kwargs."""

    print("\nDataset Description")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def udf_demo():
    """Demonstrate UDF, *args, **kwargs and __doc__."""

    if not data_1d:
        print("No Data Available!")
        return

    avg = calculate_average(*data_1d)

    show_description(
        Count=len(data_1d),
        Average=round(avg, 2),
        Minimum=min(data_1d),
        Maximum=max(data_1d)
    )

    print("\nFunction Documentation:")
    print(calculate_average.__doc__)


# ------------------------------
# Recursion Functions
# ------------------------------
def factorial(n):
    """Calculate factorial recursively."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate fibonacci recursively."""

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def recursion_menu():
    print("\n1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter Choice: ")

    num = int(input("Enter Number: "))

    if choice == "1":
        print("Factorial =", factorial(num))

    elif choice == "2":
        print("Fibonacci =", fibonacci(num))

    else:
        print("Invalid Choice!")


# ------------------------------
# Lambda Function
# ------------------------------
def filter_data():
    """Filter values above threshold using lambda."""

    if not data_1d:
        print("No Data Available!")
        return

    threshold = int(input("Enter Threshold Value: "))

    filtered = list(filter(lambda x: x > threshold, data_1d))

    print("Filtered Data:", filtered)

    transformed = list(map(lambda x: x * 2, filtered))

    print("Mapped Data (x2):", transformed)


# ------------------------------
# Global Keyword
# ------------------------------
def update_summary():
    """Store summary using global keyword."""

    global summary

    if not data_1d:
        print("No Data Available!")
        return

    summary = {
        "Count": len(data_1d),
        "Sum": sum(data_1d),
        "Average": round(sum(data_1d) / len(data_1d), 2)
    }

    print("Global Summary Updated!")
    print(summary)


# ------------------------------
# Return Multiple Values
# ------------------------------
def statistics():
    """Return multiple values."""

    minimum = min(data_1d)
    maximum = max(data_1d)
    total = sum(data_1d)
    average = round(total / len(data_1d), 2)

    return minimum, maximum, total, average


def display_statistics():
    if not data_1d:
        print("No Data Available!")
        return

    mn, mx, total, avg = statistics()

    print("\n----- STATISTICS -----")
    print("Minimum :", mn)
    print("Maximum :", mx)
    print("Sum     :", total)
    print("Average :", avg)


# ------------------------------
# Display 2D Array
# ------------------------------
def display_2d():
    """Display 2D Array."""

    if not data_2d:
        print("No 2D Data Available!")
        return

    print("\n2D Array:")

    for row in data_2d:
        print(row)


# ------------------------------
# Sorting Function
# ------------------------------
def sort_data():
    """Sort dataset."""

    if not data_1d:
        print("No Data Available!")
        return

    print("\n1. Ascending")
    print("2. Descending")

    choice = input("Choose Option: ")

    if choice == "1":
        print("Sorted Data:", sorted(data_1d))

    elif choice == "2":
        print("Sorted Data:", sorted(data_1d, reverse=True))

    else:
        print("Invalid Choice!")


# ------------------------------
# Main Menu
# ------------------------------
def main():

    while True:

        print("\n" + "=" * 50)
        print("DATA ANALYZER AND TRANSFORMER PROGRAM")
        print("=" * 50)

        print("1. Input 1D Array")
        print("2. Input 2D Array")
        print("3. Display Summary")
        print("4. UDF Demo")
        print("5. Recursion Functions")
        print("6. Lambda Filter")
        print("7. Global Summary")
        print("8. Return Multiple Values")
        print("9. Display 2D Array")
        print("10. Sort Data")
        print("0. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            input_1d()

        elif choice == "2":
            input_2d()

        elif choice == "3":
            display_summary()

        elif choice == "4":
            udf_demo()

        elif choice == "5":
            recursion_menu()

        elif choice == "6":
            filter_data()

        elif choice == "7":
            update_summary()

        elif choice == "8":
            display_statistics()

        elif choice == "9":
            display_2d()

        elif choice == "10":
            sort_data()

        elif choice == "0":
            print("Thank You For Using The Program!")
            break

        else:
            print("Invalid Choice!")


# Program Start
main()
