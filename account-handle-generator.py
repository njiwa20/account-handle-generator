
def get_account_and_dob():
    name = input("Enter your desired account name: ")
    dob = input("Enter your date of birth (MM/DD/YYYY): ")
    return name, dob

def format_account_name(username):
    username = username[:10]
    username = username.lower()
    username = username.replace(" ", "_")
    return username

def finalize_account_name(formatted_name, dob):
    last_two = dob[-2:]
    return formatted_name + last_two

name, dob = get_account_and_dob()
formatted = format_account_name(name)
final_name = finalize_account_name(formatted, dob)

print("Your account has been created.")
print("Your account handle is: " + final_name)