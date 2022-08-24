from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = item['question']
    answer = item['correct_answer']
    question_bank.append(Question(question, answer))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print('Congratulations on completing the quiz!')
print(f'Your final score is: {quiz.score}/{quiz.question_number}')



