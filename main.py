from ui import QuizInterface
from data import question_data
from question_model import Questions
from quizbrain import Quizbrain

question_bank = []

# Iterate over the question data to populate the question bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Questions(question_text,question_answer)
    question_bank.append(new_question)

quizBrain = Quizbrain(question_bank)
quizUi = QuizInterface(quizBrain)