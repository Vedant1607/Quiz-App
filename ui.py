from tkinter import *
from quizbrain import Quizbrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self,quizbrain:Quizbrain):
        self.quiz = quizbrain # Quizbrain instance to manage quiz logic
        
        # Set up the main window
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        
        # Label to display the current score
        self.scoreLabel = Label(text="Score: 0",bg=THEME_COLOR, font=("Ariel",15,"bold"),fg="white")
        self.scoreLabel.grid(row=0,column=1)
        
        # Canvas to display the quiz question
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.questionText = self.canvas.create_text(150,125,width=250,text="Question goes here",font=("Ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        # Button to give our answer
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img,highlightthickness=0,command=self.truePressed)
        self.true_button.grid(row=2,column=0)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,highlightthickness=0,command=self.falsePressed)
        self.false_button.grid(row=2,column=1)
        
        self.getNextQuestion()
        
        # Start the tkinter event loop
        self.window.mainloop()
    
    def getNextQuestion(self):
        # Fetch the next question if there are more left
        self.scoreLabel.config(text=f"Score: {self.quiz.score}")
        if self.quiz.stil_has_question():
            self.canvas.config(bg="white") # Reset the canvas background color
            question_text = self.quiz.nextQuestion()
            self.canvas.itemconfig(self.questionText, text=question_text)
        else:
            self.canvas.itemconfig(self.questionText,text="You've completed the quiz")
            # Disable the buttons to prevent further interactions
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def truePressed(self):
        # Check if the answer "True" is correct and provide feedback
        is_right = self.quiz.checkAnswer("True")
        self.giveFeedback(is_right)
        
    def falsePressed(self):
        # Check if the answer "False" is correct and provide feedback
        is_right = self.quiz.checkAnswer("False")
        self.giveFeedback(is_right)
    
    def giveFeedback(self,is_right):
        # Provide visual feedback based on whether the answer is correct
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Wait for 1 second before moving to the next question
        self.window.after(ms=1000, func=self.getNextQuestion)