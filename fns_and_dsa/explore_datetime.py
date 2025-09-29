from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_datetime}")
    return formatted_datetime

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")
    return formatted_future_date

def main():
    print("=== DateTime Explorer ===\n")
    
    # Part 1: Display the Current Date and Time
    print("Part 1: Current Date and Time")
    display_current_datetime()
    print()
    
    # Part 2: Calculate a Future Date
    print("Part 2: Calculate Future Date")
    try:
        # Prompt user to enter number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        # Calculate and display the future date
        calculate_future_date(days_to_add)
        
    except ValueError:
        print("Error: Please enter a valid integer for the number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
