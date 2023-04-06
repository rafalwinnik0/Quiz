class QuizBrain:

    def __init__(self, points):
        self.points = points

    def check_answer(self, answer, question):
        if answer == question.answer:
            print("You got it right!")
            self.points += 1
        else:
            print("That's wrong.")

    def display_result(self, number, question):
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.points}/{number}")
        print()
