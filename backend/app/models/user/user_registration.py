
# User Registration

def register_user():
    """
    Function to handle user registration.
    This function will validate the user data and create a new user in the database.
    """


# Validate the user data, check if the user already exists
def is_email_taken(email): #bool??
    pass
    # If yes, return an error message | "This email is already in use."
    # If no, proceed

def is_username_taken(username): #bool??
    pass
    # If yes, return an error message | "This username is already in use."
    # If no, proceed    

# Example of a simple registration logic:
'''
    user_data = {
        "username": "new_user",
        "email": "new_user@example.com",
        "password": "secure_password"
    }
'''

if(is_username_taken() and is_email_taken()) == False:
    trigger_registration()

def trigger_registration():
    pass




# Hash the password


# Save the user to the database.
