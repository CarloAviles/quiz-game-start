from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for item in question_data:
    question = Question(item['question'], item['correct_answer'])
    question_bank.append(question)

QuizBrain(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_next_question():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")






