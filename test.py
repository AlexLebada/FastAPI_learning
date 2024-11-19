from datetime import datetime

items = []

items_2= ['mere','pere']

current_date = datetime.now()
current_year = current_date.year
end_of_year = datetime(current_year, 12, 31)
days_left = (end_of_year - current_date).days
days_elapsed = 365 - days_left
print(current_date)