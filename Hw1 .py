from datetime import datetime
def get_days_from_today(date):


    target_date = datetime.strptime(date, '%Y-%m-%d').date()
    today = datetime.today().date()
    delta = today - target_date
    return delta.days
if __name__ == "__main__":
    print(get_days_from_today("2024-11-01"))  
