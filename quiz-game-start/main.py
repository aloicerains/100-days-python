from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question bank to hold a list of question objects
question_bank = [Question(q.get('question'), q.get('correct_answer')) for q in question_data]
new_question = QuizBrain(question_bank)
while new_question.still_has_questions():
    new_question.next_question()
print("You've completed the quiz")
final_score = (new_question.score/new_question.question_number) * 100
print(f"Final score was {final_score}%")
