from datetime import datetime

def assess_target(kms: int, target: int) -> str:
    current_date = datetime.now()
    current_year = current_date.year

    end_of_year = datetime(current_year, 12, 31)
    days_left = (end_of_year - current_date).days
    days_elapsed = 365 - days_left

    todays_target = target / 365 * days_elapsed
    status = kms - todays_target

    message = (f"You are on target by {status:.2f}" if status >= 0
               else f"You are short of target by {status * -1:2f}"  # positive val.
               )

    return message