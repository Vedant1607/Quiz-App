import html
class Quizbrain:
    
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
    
    def stil_has_question(self): # Check if there are still questions left in the quiz
        return self.question_number < len(self.question_list)
    
    # Retrieve the next question from the list
    def nextQuestion(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text) # Decode HTML entities in the question text
        return f"{self.question_number}: {q_text}"
    
    # Compare the user's answer with the correct answer
    def checkAnswer(self,answer):
        correctAnswer = self.current_question.answer
        if answer.lower() == correctAnswer.lower():
            self.score += 1
            return True
        else:
            False