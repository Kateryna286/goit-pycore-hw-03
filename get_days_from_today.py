import datetime

def get_days_from_today(date):
    today = datetime.date.today()
    target_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    delta = today - target_date

    return delta.days
