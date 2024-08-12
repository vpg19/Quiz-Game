THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.window.title('Quizzler')
        self.score = Label(text='Score: 0',bg=THEME_COLOR,highlightthickness=0,font = ('Ariel',15,'normal'),fg='white')
        self.score.grid(column=1,row=0)
        self.canvas = Canvas(width=300,height=250,bg='white',highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,width=280,text='Question Here',fill=THEME_COLOR,font=('Ariel',15,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=40)
        right_img = PhotoImage(file = 'Code\\Quizzler\\images\\true.png')
        self.right = Button(image=right_img,highlightthickness=0,command=self.true_pressed)
        self.right.grid(column=0,row=3)
        wrong_img = PhotoImage(file = 'Code\\Quizzler\\images\\false.png')
        self.wrong = Button(image=wrong_img,highlightthickness=0,command=self.false_pressed)
        self.wrong.grid(column=1,row=3)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
            self.canvas.config(bg='white')
        else:
            self.right.config(state='disabled')
            self.wrong.config(state='disabled')
            if messagebox.showinfo(title = 'Quiz End',message=f'You have reached the end of the quiz !!\nYour score is {self.quiz.score}/10 '):
                self.window.destroy()
            
    def true_pressed(self):
        if self.quiz.check_answer('True'):
            self.canvas.config(bg='green')
            self.score.config(text=f'Score: {self.quiz.score}')
            self.window.after(1000,func=self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000,func=self.get_next_question)
    def false_pressed(self):
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='green')
            self.score.config(text=f'Score: {self.quiz.score}')
            self.window.after(1000,func=self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000,func=self.get_next_question)
# QuizInterface()