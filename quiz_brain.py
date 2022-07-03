class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You have completed the quiz")
            print(f"Your final score was {self.score} from {self.question_number} questions.")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it!")
            print(f"Questions: {self.question_number}, Score: {self.score}")
        else:
            print("Sorry, you were wrong!")
            print(f"Questions: {self.question_number}, Score: {self.score}")
        print(f"The correct answer is {correct_answer}")
        print("\n")
