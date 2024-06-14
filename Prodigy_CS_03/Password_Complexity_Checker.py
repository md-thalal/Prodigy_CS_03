import re

def check_password_complexity(password):
    # Define criteria for password strength
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*()-_=+{};:,<.>]", password)

    # Provide feedback based on criteria
    if length_error:
        return "Password must be at least 8 characters long."
    elif uppercase_error:
        return "Password must contain at least one uppercase letter."
    elif lowercase_error:
        return "Password must contain at least one lowercase letter."
    elif digit_error:
        return "Password must contain at least one digit."
    elif special_char_error:
        return "Password must contain at least one special character."
    else:
        return "Password meets complexity requirements."

# Example usage
password = input("Enter your password: ")
result = check_password_complexity(password)
print(result)
