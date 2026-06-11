from models.result import Result
from utils.file_handler import load_data, save_data

import random


def start_quiz(username, category, difficulty):

    questions = load_data("data/questions.pkl")

    filtered_questions = []

    for question in questions:

        if (
            question.category.upper() == category.upper()
            and
            question.difficulty.upper() == difficulty.upper()
        ):

            filtered_questions.append(question)

    if len(filtered_questions) == 0:

        print("\nNo Questions Found!")
        return

    selected_questions = random.sample(
        filtered_questions,
        min(10, len(filtered_questions))
    )

    score = 0
    wrong_answers = []

    for question in selected_questions:

        print("\n------------------------")

        print(question.question_text)

        print("A.", question.option_a)
        print("B.", question.option_b)
        print("C.", question.option_c)
        print("D.", question.option_d)

        answer = input(
            "Enter Answer (A/B/C/D): "
        ).upper()

        if answer == question.correct_answer.upper():

            print("Correct!")
            score += 1

        else:

            print("Wrong!")

            wrong_answers.append(
                (
                    question.question_text,
                    answer,
                    question.correct_answer
                )
            )

    print("\n===== QUIZ COMPLETED =====")

    print(
        f"Score : {score}/{len(selected_questions)}"
    )

    percentage = (
        score / len(selected_questions)
    ) * 100

    print(
        f"Percentage : {percentage:.2f}%"
    )

    if percentage >= 80:
        grade = "A"

    elif percentage >= 60:
        grade = "B"

    elif percentage >= 40:
        grade = "C"

    else:
        grade = "Fail"

    print("Grade :", grade)

    results = load_data(
        "data/results.pkl"
    )

    result = Result(
        username,
        score,
        len(selected_questions),
        percentage,
        grade
    )

    results.append(result)

    save_data(
        "data/results.pkl",
        results
    )

    if wrong_answers:

        print(
            "\n===== WRONG ANSWER REVIEW ====="
        )

        for question, user_answer, correct_answer in wrong_answers:

            print("\nQuestion:")
            print(question)

            print(
                "Your Answer:",
                user_answer
            )

            print(
                "Correct Answer:",
                correct_answer
            )


def view_quiz_history(username):

    results = load_data(
        "data/results.pkl"
    )

    found = False

    print("\n===== QUIZ HISTORY =====")

    attempt = 1

    for result in results:

        if result.username == username:

            found = True

            print(
                f"\nAttempt {attempt}"
            )

            print(
                "Score:",
                f"{result.score}/{result.total_questions}"
            )

            print(
                "Percentage:",
                f"{result.percentage:.2f}%"
            )

            print(
                "Grade:",
                result.grade
            )

            print("----------------------")

            attempt += 1

    if not found:

        print(
            "No Quiz History Found!"
        )


def view_leaderboard():

    results = load_data(
        "data/results.pkl"
    )

    if not results:

        print("No Results Found!")
        return

    leaderboard = {}

    for result in results:

        username = result.username

        if (
            username not in leaderboard
            or
            result.percentage >
            leaderboard[username]
        ):

            leaderboard[username] = (
                result.percentage
            )

    sorted_leaderboard = sorted(
        leaderboard.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print(
        "\n===== LEADERBOARD ====="
    )

    rank = 1

    for username, percentage in sorted_leaderboard:

        print(
            f"{rank}. {username} - {percentage:.2f}%"
        )

        rank += 1


def view_statistics():

    results = load_data(
        "data/results.pkl"
    )

    users = load_data(
        "data/users.pkl"
    )

    if not results:

        print(
            "No Statistics Available!"
        )

        return

    total_attempts = len(results)

    total_users = len(users)

    highest_score = max(
        result.percentage
        for result in results
    )

    average_score = (
        sum(
            result.percentage
            for result in results
        )
        /
        total_attempts
    )

    print(
        "\n===== STATISTICS DASHBOARD ====="
    )

    print(
        "Total Quiz Attempts :",
        total_attempts
    )

    print(
        "Total Registered Users :",
        total_users
    )

    print(
        "Highest Score :",
        f"{highest_score:.2f}%"
    )

    print(
        "Average Score :",
        f"{average_score:.2f}%"
    )


def user_performance(username):

    results = load_data(
        "data/results.pkl"
    )

    user_results = []

    for result in results:

        if result.username == username:

            user_results.append(
                result.percentage
            )

    if not user_results:

        print(
            "No Performance Data Found!"
        )

        return

    print(
        "\n===== YOUR PERFORMANCE ====="
    )

    print(
        "Total Attempts :",
        len(user_results)
    )

    print(
        "Best Score :",
        f"{max(user_results):.2f}%"
    )

    print(
        "Worst Score :",
        f"{min(user_results):.2f}%"
    )

    print(
        "Average Score :",
        f"{sum(user_results) / len(user_results):.2f}%"
    )


def select_difficulty():

    print("\n===== SELECT DIFFICULTY =====")

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input(
        "Enter Choice: "
    )

    if choice == "1":
        return "EASY"

    elif choice == "2":
        return "MEDIUM"

    elif choice == "3":
        return "HARD"

    else:

        print("Invalid Choice!")
        return None


def user_menu(username):

    while True:

        print("\n===== USER MENU =====")

        print("1. Python Quiz")
        print("2. Aptitude Quiz")
        print("3. General Knowledge Quiz")
        print("4. View Quiz History")
        print("5. View Leaderboard")
        print("6. View Statistics")
        print("7. My Performance")
        print("8. Logout")

        choice = input(
            "Enter Choice: "
        )

        if choice == "1":

            difficulty = select_difficulty()

            if difficulty:

                start_quiz(
                    username,
                    "PYTHON",
                    difficulty
                )

        elif choice == "2":

            difficulty = select_difficulty()

            if difficulty:

                start_quiz(
                    username,
                    "APTITUDE",
                    difficulty
                )

        elif choice == "3":

            difficulty = select_difficulty()

            if difficulty:

                start_quiz(
                    username,
                    "GENERAL KNOWLEDGE",
                    difficulty
                )

        elif choice == "4":

            view_quiz_history(
                username
            )

        elif choice == "5":

            view_leaderboard()

        elif choice == "6":

            view_statistics()

        elif choice == "7":

            user_performance(
                username
            )

        elif choice == "8":

            print(
                "User Logged Out"
            )

            break

        else:

            print(
                "Invalid Choice!"
            )