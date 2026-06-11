from services.auth_service import register_user, login_user
from services.admin_service import admin_login, admin_menu
from services.quiz_service import user_menu


while True:

    print("\n===== QUIZ MASTER PRO =====")

    print("1. Register")
    print("2. Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        register_user()

    elif choice == "2":

        user = login_user()

        if user:

            print(
                "Welcome",
                user.username
            )

            user_menu(user.username)

    elif choice == "3":

        if admin_login():

            admin_menu()

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")


