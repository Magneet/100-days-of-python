from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from random import choice
question_bank = []
for i in question_data:
    ii = Question(i["text"], i["answer"])
    question_bank.append(ii)

quiz = QuizBrain(question_bank)
while quiz.questions_remaining():
    quiz.next_question()
print("QUiz completed")
print(f"Final score is {quiz.score}")



