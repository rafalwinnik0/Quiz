from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_brain = QuizBrain(0)
question_number = 1
# points = 0

for question in question_data:
    new_question = Question(question['text'], question['answer'])
    answer = input(f"Q{question_number}: {new_question.question}(True/False): ")
    quiz_brain.check_answer(answer, new_question)
    quiz_brain.display_result(question_number, new_question)
    question_number += 1

# print("You've completed the quiz")
# print(f"Your final score was: {points}/{question_number}")
