from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
THEME_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 16)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.user_answer = None
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(self.window, text="Score: 0", font=SCORE_FONT, background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background="White")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=THEME_FONT, fill=THEME_COLOR)

        # BUTTONS

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_guess)
        self.true_button.grid(column=1, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_guess)
        self.false_button.grid(column=0, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="White")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_guess(self):
        self.user_answer = "true"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def false_guess(self):
        self.user_answer = "false"
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, func=self.get_next_question)
