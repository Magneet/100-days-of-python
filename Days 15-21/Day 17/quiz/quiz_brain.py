class QuizBrain:

        def __init__(self, q_list):
            self.question_number = 0
            self.question_list = q_list
            self.score = 0

        def next_question(self):
            current_question = self.question_list[self.question_number]
            self.question_number += 1 
            u_answer = input(f"{self.question_number}: is {current_question.text} (True or False)?")
            u_answer = u_answer.lower()
            self.check_answer(current_question.answer, u_answer)

        def questions_remaining(self):
            return self.question_number < len(self.question_list)

        def check_answer(self,current_question, u_answer):
            correct_answer = current_question
            correct_answer = correct_answer.lower()
            if u_answer == correct_answer:
                print("correct")
                self.score += 1
            else:
                print("Wrong!")
            print(f"The correct answer was: {correct_answer}")
            print(f"You score is {self.score}")
            print("\n")







