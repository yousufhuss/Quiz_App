import tkinter as tk
from tkinter import messagebox
import threading


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.questions = [
            ("What is the capital of Malawi?", "Lilongwe"),
            ("What is 20 + 8?", "28"),
            ("What is the color of water?", "Colorless"),
            ("What was the first capital city of Malawi?", "Zomba"),
            ("How many times muslims pray in a day?", "5 times"),

        ]
        self.current_question = 0
        self.score = 0
        self.total_time = 40  # total time for the quiz in seconds

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=30)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer , background="yellow")
        self.submit_button.pack(pady=10)

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.timer_label.pack(pady=30)

        self.start_quiz()

    def start_quiz(self):
        self.time_left = self.total_time
        self.next_question()
        self.update_timer()

    def next_question(self):
        if self.current_question < len(self.questions):
            self.question, self.answer = self.questions[self.current_question]
            self.question_label.config(text=self.question)
            self.answer_entry.delete(0, tk.END)
            self.answered = False
        else:
            self.end_quiz()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.root.after(1000, self.update_timer)
        else:
            self.end_quiz()

    def check_answer(self):
        if not self.answered and self.current_question < len(self.questions):
            user_answer = self.answer_entry.get().strip()
            if user_answer.lower() == self.answer.lower():
                self.score += 1
                messagebox.showinfo("Correct!", "Correct!")
            else:
                messagebox.showinfo("Wrong!", f"Wrong! The correct answer was: {self.answer}")
            self.answered = True
            self.current_question += 1
            self.next_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"Quiz over! Your final score is: {self.score}/{len(self.questions)}")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
