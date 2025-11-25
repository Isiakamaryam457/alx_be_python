from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current date and time, saves the date in current_date,
    and prints the full timestamp in 'YYYY-MM-DD HH:MM:SS' format.
    """
    now = datetime.now()
    current_date = now.date
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_now}")
    return current_date

def calculate_future_date(days):
    """
    Takes a number of days, calculates the future date,
    saves it in future_date, and prints it in 'YYYY-MM-DD' format.
    """

    today = datetime.now().date()
    future_date = today + timedelta(days=days)
    print(f"Future date after {days} days: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    current_date = display_current_datetime()

    days_input = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_input)


if __name__ == "__main__":
    main()


