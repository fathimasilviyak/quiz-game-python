from question_model import Question
from data import question_data
from question_brain import QuizBrain

# Create question bank of question objects
question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)
# print(question_bank[0].answer)

# Create object for QuizBrain to bring up new question
quiz = QuizBrain(question_bank)

# Bring up the question and ask user to answer it
# quiz.next_question()

# Repeat asking questions until all the questions in the question bank are asked
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
