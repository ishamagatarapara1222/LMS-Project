import datetime
import time

def get_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_date_difference(date_str1, date_str2):
    try:
        d1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
        return f"Difference: {abs((d2 - d1).days)} days"
    except ValueError:
        return "Error: Please use YYYY-MM-DD format."

def format_custom_date(format_str="%d-%B-%Y"):
    return datetime.datetime.now().strftime(format_str)

def start_stopwatch_and_countdown(seconds):
    print(class_name:="Countdown Started...")
    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining...")
        time.sleep(1)
    print("Time's up!")
        
