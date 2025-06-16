import re
def check_password(password):
    if len(password) < 8:
        return "weak: passward must be at least 8 chars"
    if not any(char.isdigit() for char in password):
        return "weak: passward must contain at least one digit"
    if not any(char.isupper() for char in password):
        return "weak: passward must contain an uppercase letter"
    if not any(char.islower() for char in password):
        return "weak: passward must contain a lowercase letter"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "medium: passward must contain at least one special character"
    return "strong: passward is secure"
def passward_checker():
    print("Welcome to the password checker!")
    while True:
        password = input("Please enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Thank you for using this tool!")
            break
        result = check_password(password)
        print(result)
if __name__ == "__main__":
    passward_checker()

