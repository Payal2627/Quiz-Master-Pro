from models.question import Question
from utils.file_handler import load_data, save_data


def admin_login():

    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    if username == "admin" and password == "admin123":
        print("Admin Login Successful!")
        return True

    print("Invalid Admin Credentials!")
    return False


def add_question():

    questions = load_data("data/questions.pkl")

    question_id = input("Enter Question ID: ")

    question_text = input("Enter Question: ")

    option_a = input("Option A: ")
    option_b = input("Option B: ")
    option_c = input("Option C: ")
    option_d = input("Option D: ")

    correct_answer = input(
        "Correct Answer (A/B/C/D): "
    ).upper()

    category = input("Category: ")

    difficulty = input(
        "Difficulty (Easy/Medium/Hard): "
    )

    question = Question(
        question_id,
        question_text,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        category,
        difficulty
    )

    questions.append(question)

    save_data(
        "data/questions.pkl",
        questions
    )

    print("Question Added Successfully!")


def view_questions():

    questions = load_data("data/questions.pkl")

    if not questions:
        print("No Questions Found!")
        return

    for question in questions:

        print("\n----------------------")

        question.display_question()


def admin_menu():

    while True:

        print("\n===== ADMIN MENU =====")

        print("1. Add Question")
        print("2. View Questions")
        print("3. Search Question")
        print("4. Edit Question")
        print("5. Delete Question")
        print("6. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_question()

        elif choice == "2":
            view_questions()

        elif choice == "3":
            search_question()

        elif choice == "4":
            edit_question()

        elif choice == "5":
            delete_question()

        elif choice == "6":
            print("Admin Logged Out")
            break

        else:
            print("Invalid Choice!")


def search_question():

    questions = load_data("data/questions.pkl")

    search_id = input(
        "Enter Question ID to Search: "
    )

    for question in questions:

        if question.question_id == search_id:

            print("\nQuestion Found!")

            question.display_question()

            return

    print("Question Not Found!")


def delete_question():

    questions = load_data("data/questions.pkl")

    delete_id = input(
        "Enter Question ID to Delete: "
    )

    for question in questions:

        if question.question_id == delete_id:

            questions.remove(question)

            save_data(
                "data/questions.pkl",
                questions
            )

            print(
                "Question Deleted Successfully!"
            )

            return

    print("Question Not Found!")


def edit_question():

    questions = load_data("data/questions.pkl")

    edit_id = input(
        "Enter Question ID to Edit: "
    )

    for question in questions:

        if question.question_id == edit_id:

            print(
                "\nEnter New Details"
            )

            question.question_text = input(
                "Question: "
            )

            question.option_a = input(
                "Option A: "
            )

            question.option_b = input(
                "Option B: "
            )

            question.option_c = input(
                "Option C: "
            )

            question.option_d = input(
                "Option D: "
            )

            question.correct_answer = input(
                "Correct Answer: "
            ).upper()

            save_data(
                "data/questions.pkl",
                questions
            )

            print(
                "Question Updated Successfully!"
            )

            return

    print("Question Not Found!")