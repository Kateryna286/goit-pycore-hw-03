import datetime

def get_days_from_today(date):
    today = datetime.date.today()
    print("Today>>>", today)
    
    target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    print("Target Date>>>", target_date)
    
    delta = today - target_date
    return delta.days

print(get_days_from_today('2025-10-01'))
