from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        bdate = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        try:
            bdate_this_year = bdate.replace(year=today.year)
        except ValueError:
            bdate_this_year = bdate.replace(year=today.year, month=3, day=1)

        if bdate_this_year < today:
            try:
                bdate_this_year = bdate.replace(year=today.year + 1)
            except ValueError:
                bdate_this_year = bdate.replace(year=today.year + 1, month=3, day=1)

        if 0 <= (bdate_this_year - today).days <= 7:
            if bdate_this_year.weekday() == 5:
                bdate_this_year += timedelta(days=2)
            elif bdate_this_year.weekday() == 6:
                bdate_this_year += timedelta(days=1)
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": bdate_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

if __name__ == "__main__":
    test_users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Dmytro Salimon", "birthday": datetime.today().strftime("1995.%m.%d")}
    ]
    
    print(get_upcoming_birthdays(test_users))