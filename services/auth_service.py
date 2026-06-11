from models.user import User
from utils.file_handler import load_data, save_data
from utils.validations import (
    validate_username,
    validate_password
)


def register_user():

    users = load_data("data/users.pkl")

    username = input("Enter Username: ")

    # Username validation
    if not validate_username(username):

        print(
            "Username must be at least 3 characters."
        )

        return

    # Duplicate username check
    for user in users:

        if user.username == username:

            print(
                "Username already exists!"
            )

            return

    password = input("Enter Password: ")

    # Password validation
    if not validate_password(password):

        print(
            "Password must be at least 4 characters."
        )

        return

    confirm_password = input(
        "Confirm Password: "
    )

    # Password match check
    if password != confirm_password:

        print(
            "Passwords do not match!"
        )

        return

    new_user = User(
        username,
        password
    )

    users.append(
        new_user
    )

    save_data(
        "data/users.pkl",
        users
    )

    print(
        "Registration Successful!"
    )


def login_user():

    users = load_data(
        "data/users.pkl"
    )

    username = input(
        "Enter Username: "
    )

    password = input(
        "Enter Password: "
    )

    for user in users:

        if (
            user.username == username
            and
            user.password == password
        ):

            print(
                "Login Successful!"
            )

            return user

    print(
        "Invalid Username or Password!"
    )

    return None