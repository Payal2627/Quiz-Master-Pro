class Result:

    def __init__(
            self,
            username,
            score,
            total_questions,
            percentage,
            grade):

        self.username = username
        self.score = score

        self.total_questions = total_questions

        self.percentage = percentage

        self.grade = grade

    def display_result(self):

        print("\nResult Details")

        print("Username:", self.username)
        print("Score:", self.score)

        print("Total Questions:", self.total_questions)

        print("Percentage:", self.percentage)

        print("Grade:", self.grade)