from question_model import Question
from data import question_data_trivia
from quiz_brain import QuizBrain

question_bank = []
for item in question_data_trivia:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)


def print_answer_sheet():
    for question in question_bank:
        print(question.text)
        print(question.answer)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
