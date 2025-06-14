from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.06.28"},
    {"name": "Jane Smith", "birthday": "1990.06.19"},
    {"name": "Alice Johnson", "birthday": "1992.06.15"},
    {"name": "Bob Brown", "birthday": "2008.02.22"},
    {"name": "Charlie Black", "birthday": "2000.06.21"},
]

# перевести дати народження в формат YYYY.MM.DD
# змінити роки народження на поточний рік, щоб зрозуміти, коли буде наступний день народження
# знайти дні народження, які будуть в найближчі 7 днів від поточного дня
# перевірити, чи дата припадає на вихідні і якщо так, то дата привітання переноситься на наступний понеділок
# вивести список словників, де кожен словник містить інформацію про користувача (ключ name) 
# та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
# функція має працювати, якщо наступні 7 днів знаходяться на зламі років, наприклад, якщо сьогодні 27 грудня, а день народження 1 січня наступного року.


def get_upcoming_birthdays(users):
    today = datetime.now().date()
    print(f"Today's week's day: {today.weekday()}")

    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], '%Y.%m.%d').date()
        except ValueError:
            print(f"Invalid date format for {user['name']}: {user['birthday']}. Expected 'YYYY.MM.DD'")
            continue

        # Set birthday to this year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday has already passed this year, set it to next year
        if birthday_this_year < today:
            print(f"Birthday for {user['name']} ти вже пропустила :()")
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference in days
        days_until_birthday = (birthday_this_year - today).days
        print(f"Days until {user['name']}'s birthday: {days_until_birthday}")

        # Check if the birthday is within the next 7 days
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            # Check if the congratulation date falls on a weekend
            if congratulation_date.weekday() >= 5:
                print(f"ДН {user['name']} в {congratulation_date.weekday()}")

                # If it's Saturday (5) or Sunday (6), move to the next Monday
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime('%Y.%m.%d')
            })              

    return upcoming_birthdays   

print(get_upcoming_birthdays(users))