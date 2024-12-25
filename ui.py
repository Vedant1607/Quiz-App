from tkinter import *

THEME_COLOR = "#375362"

class Quiz:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        
        self.scoreLabel = Label(text="Score: 0",bg=THEME_COLOR, font=("Ariel",15,"bold"),fg="white")
        self.scoreLabel.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.canvas.create_text(150,125,width=250,text="Question goes here",font=("Ariel",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        true_img = PhotoImage(file="images/true.png")
        self.ture_button = Button(image=true_img,highlightthickness=0)
        self.ture_button.grid(row=2,column=0)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,highlightthickness=0)
        self.false_button.grid(row=2,column=1)
        
        self.window.mainloop()