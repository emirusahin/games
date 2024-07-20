from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# MY WAY
# for dictionary in question_data:
#     q = Question()
#     for key in dictionary:
#         if key == "text":
#             q.text = dictionary[key]
#         if key == "answer":
#             q.answer = dictionary[key]
#         question_bank.append(q)


# BETTER WAY
for dictionary in question_data:
    question_text = dictionary["question"]
    question_answer = dictionary["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
