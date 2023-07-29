# # Format and validate personal information
# first_name = user_input["First Name"]
# last_name = user_input["Last Name"]
# phone_number = re.sub(r'\D', '', user_input["Phone Number"])
# email_address = user_input["Email"]

# fullname = '{} {}'.format(first_name.capitalize(), last_name.capitalize())
# if len(phone_number) != 11:
#     raise ValueError("Phone number must have 11 digits.")
# if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
#     raise ValueError("Invalid email address.")