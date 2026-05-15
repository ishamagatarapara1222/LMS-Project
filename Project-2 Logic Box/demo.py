# =========================================
# Project: Logic Box
# Pattern Generator and Number Analyzer
# =========================================

print("Welcome to the Pattern Generator and Number Analyzer!")

# menu loop
while True:

    print("\n----------------------------")
    print("1. Generate a Pattern")
    print("2. Analyze Numbers")
    print("3. Exit")
    print("----------------------------")

    choice = input("Enter your choice: ")

    # =====================================
    # OPTION 1 - PATTERN GENERATOR
    # =====================================
    if choice == "1":

        rows = int(input("Enter number of rows: "))

        # validation
        if rows <= 0:
            print("Invalid input. Rows must be greater than 0.")

        else:
            print("\nRight-Angled Triangle Pattern:\n")

            # nested loop for pattern
            for i in range(1, rows + 1):

                for j in range(i):
                    print("*", end="")

                print()

    # =====================================
    # OPTION 2 - NUMBER ANALYZER
    # =====================================
    elif choice == "2":

        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        # validation
        if end < start:
            print("Ending number must be greater than starting number.")

        else:

            total = 0

            print("\nNumber Analysis:\n")

            # loop through numbers
            for number in range(start, end + 1):

                # use of continue
                if number == 0:
                    continue

                # odd or even check
                if number % 2 == 0:
                    print(number, "is Even")
                else:
                    print(number, "is Odd")

                # adding numbers
                total = total + number

                # use of pass statement
                pass

            print("\nSum of all numbers from", start, "to", end, "is:", total)

    # =====================================
    # OPTION 3 - EXIT
    # =====================================
    elif choice == "3":

        print("\nThank you for using the program.")
        print("Goodbye!")
        break

    # =====================================
    # INVALID INPUT
    # =====================================
    else:
        print("Invalid choice. Please try again.")
