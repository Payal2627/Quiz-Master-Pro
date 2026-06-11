class Question:

    def __init__(
            self,
            question_id,
            question_text,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            category,
            difficulty):

        self.question_id = question_id
        self.question_text = question_text

        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d

        self.correct_answer = correct_answer

        self.category = category
        self.difficulty = difficulty

    def display_question(self):

        print("\nQuestion ID:", self.question_id)
        print("Question:", self.question_text)

        print("A.", self.option_a)
        print("B.", self.option_b)
        print("C.", self.option_c)
        print("D.", self.option_d)

        print("Answer:", self.correct_answer)
        print("Category:", self.category)
        print("Difficulty:", self.difficulty)