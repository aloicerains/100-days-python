THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

CANVAS_FONT = ("Arial", 20, "italic")
class Quizinterface:
    def __init__(self, quizes: QuizBrain):
        self.quiz = quizes
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # create canvas
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        # the width in the quiz_text allows wrapping of text output
        self.quiz_text = self.canvas.create_text(150, 125, width=280, font=CANVAS_FONT)
        # locate canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white')
        # locate score label
        self.score_label.grid(row=0, column=1)

        # buttons
        true_btn_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=true_btn_img, highlightthickness=0, command=self.check_true)
        false_btn_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, command=self.check_false)
        # locate buttons
        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_quiz()

        self.window.mainloop()

    def get_next_quiz(self):
        self.canvas.config(bg='white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_text, text=q_text)

    def check_true(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, answer):
        self.validate_answer(answer)
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_quiz)  # calls next guiz after 1 sec
        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.quiz_text, text=f"You've completed the quiz\nTotal score: {self.quiz.score}/10")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def validate_answer(self, answer: bool):

        if answer:
            self.canvas.config(bg='green')

        else:
            self.canvas.config(bg='red')

        self.score_label.config(text=f"Score: {self.quiz.score}")

