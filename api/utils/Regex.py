def password_regex():
    """
    At least one uppercase letter
    At least one lowercase letter
    At least one digit
    Can contain any of the following special characters: !@#$%^&*()_-+=[]{}|\:;"'<>,.?/~
    """
    return r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=\[\]{}|\:;"\'<>,.?/~])[A-Za-z\d!@#$%^&*()_\-+=\[\]{}|\:;"\'<>,.?/~]{8}$'

def phone_number_regex():
    return r'^\+[1-9]\d{1,2}\d{9}$'