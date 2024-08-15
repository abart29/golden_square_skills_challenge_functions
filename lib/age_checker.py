from datetime import datetime

def age_checker(dob_string):
    if dob_string is None:
        raise Exception("no date of birth given")
    
    try:
        datetime.fromisoformat(dob_string)
    except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")


    dob = datetime.strptime(dob_string, "%Y-%m-%d")
    today = datetime.now()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age >= 16:
        return "access is granted"
    else:
        return f"access is denied, your current age is {age}, you must be at least 16 years old"