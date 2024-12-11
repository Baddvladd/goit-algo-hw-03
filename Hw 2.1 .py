from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - target_date
        return delta.days
    except ValueError:
        return "Помилка: неправильний формат дати. Використовуйте 'YYYY-MM-DD'."

if __name__ == "__main__":
    print(get_days_from_today("2024-11-01"))
    print(get_days_from_today("13.13.2000"))
