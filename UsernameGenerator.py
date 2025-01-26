from datetime import datetime

def user_details():
    """
    Prompt user input and generate a username.
    """
    valid = False
    while not valid:
        print("Insert your first name")
        first_name = input().strip()
        if not first_name.isalpha():
            print("Invalid first name")
        else:
            valid = True

    valid = False
    while not valid:
        print("Insert your last name")
        last_name = input().strip()
        if not last_name.isalpha():
            print("Invalid last name")
        else:
            valid = True

    while True:
        print("Insert your cohort")
        cohort = input().strip()
        if not cohort.isdigit() or len(cohort) != 4 or int(cohort) < datetime.now().year:
            print("Invalid cohort")
        else:
            break

    while True:
        print("Insert the campus you will be attending in")
        campus = input().strip()
        campus_code = user_campus(campus)
        if not campus_code:
            print("Invalid campus")
        else:
            break

    username = create_user_name(first_name, last_name, cohort, campus_code)
    print(username)


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username.
    """
  

    first_part = first_name[-3:] if len(first_name) >= 3 else first_name + "o" * (3 - len(first_name))
    second_part = last_name[:3] if len(last_name) >= 3 else last_name + "o" * (3 - len(last_name))
    username = f"{first_part.lower()}{second_part.lower()}{cohort}{final_campus}"
    return username


def user_campus(campus):
    """
    Return valid campus abbreviations.
    """
    campus_map = {
        "johannesburg": "JHB",
        "cape town": "CPT",
        "durban": "DBN",
        "phokeng": "PHO"
    }
    return campus_map.get(campus.lower())

if __name__ == '__main__':
    user_details()
