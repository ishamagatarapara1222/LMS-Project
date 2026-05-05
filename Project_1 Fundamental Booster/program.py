#===================================
#LMS Project-1 Fundamental Booster
#===================================

#==============Welcome Section=================

print("Welcome to the Interective Personal Data Collector..!!")
print("\nThis will collect your personal information")
print("\nPerform some calculation, and show your data typr details")
print("\nLet's get started!!")


#==========Collect information section==========

print("="*50)

name = input("Please Enter your Name:")
age_str = input("Please Enter your age:")
age = int(age_str)
height_str = input("Please Enter your height:")
height = int(height_str)
fav_num_str = input("Please Enter your favourite number:")
fav_num = int(fav_num_str)


#==============Data Processing===================

print("\n"+"="*50)
print("Processing Your data....")
print("="*50)


#calculate birth year
cur_year = 2026
birth_year = cur_year - age

#calculate height to centimetre
height_cm = height * 100

#Perform some arithmatic operation
sum_value = age + fav_num
product_value = age * fav_num

#Type conversion
height_as_int = int(height)
age_as_float = float(age)
age_as_str = str(age)

#Display result

print("\n" + "=" * 50)
print("Thank you! you here is the information we collected:")
print("=" * 50)

#Display each variables  with its type and memory address

print("\nVariables Details:")
print(f"Name:{name}->Type:{type(name)}->Address:{id(name)}")
print(f"Age:{age}->Type:{type(age)}->Address:{id(age)}")
print(f"Height:{height}->Type:{type(height)}->Address:{id(height)}")
print(f"Favourite number:{fav_num}->Type:{type(fav_num)}->Address:{id(fav_num)}")

#===========Display Conversion===========
print("\n"+"="*50)
print("Type conversion")
print("=" *50)

print(f"Height as integer:{height_as_int}->Type{type(height_as_int)}")
print(f"Age as float:{age_as_float}->Type{type(age_as_float)}")
print(f"Age as string:{age_as_str}->Type{type(age_as_str)}")

#================Display Operation===================

print("="*50)
print("Calculation")
print("="*50)

print(f"\nYour height in centimetre:{height_cm} cm")
print(f"Approximently! your birth year:{birth_year}")
print(f"\nSum of age and your favourite number:{sum_value}")
print(f"\nProduct of your age and favourite number:{product_value}")

#String concatination

greeting = "Hello , " + name + "!"
message = f"Your favourite number is {fav_num}"
print(f" -> '{greeting}'")
print(f" -> type:{type(greeting)}")
print(f" -> Address:{id(greeting)}")
print(f" -> '{message}'")
print(f" -> type:{type(message)}")
print(f" -> Address:{id(message)}")

#===============Summary Table=================
print("="*50)
print("Summary table:")
print("="*50)

print(f"\n {'variable' :<20} {'type' : <25} {'id' :<15}")
print(f"\n {'name':<20} {str(name):<20} {str(type(name)):<25} {id(name):<15}")


#========Closing message===============
print("=" * 50)
print("Thank you for using the personal data collector !!")
print("=" * 50)

print("\nYou have successfully explore:")

print("\n input() and print() functions")

print("\n String , integer and Float data types")

print("\n Atrithmetic Operation( + , - , * , /).")

print("type() and id() built-in functions")

print("String Concatination")

print("Type casting")

print("=" * 50)









