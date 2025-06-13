from datetime import datetime

def get_days_from_today(date):
    today = datetime.now().date()

    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        print(f"Invalid date format: {date}. Expected 'YYYY-MM-DD'")
        return None

    delta = today - target_date
    return delta.days

print(get_days_from_today("2025/02-02"))
print(get_days_from_today("2025-02-02"))
print(get_days_from_today("2025-22-42"))