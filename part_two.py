from tkinter import *
from tkinter import messagebox as mb
from tkinter import Label

from tkinter import ttk
import tkinter as tk





question = ["Q1. Who developed Python Programming Language?",
             "Q2. Which keyword is used for function in Python?    ",
             "Q3.Which of the following character is used to give single-line comments in Python?              ",
             "Q4.Which of the following functions is a built-in function in python?                               ",
             "Q5.In which year was the Python language developed?                      "]

options = [["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum","Niene Stom"],
           ["Function              ", "def                    ", "Brackets                 ","Define              "],
           ["//            ", "#     ", "!            ","/*          "],   
           ["factorial()     ", "print()       ", "seed()     ","sqrt()      "],
           ["1995             ", "1972      ", "1981   ", "1989    "]]


answer = [2, 1, 1, 1, 3]

root = tk.Tk()
root.geometry("1280x720")
root.title("Quiz")

root.configure(bg="white")

class Quiz:
    def __init__(self):


        

        # set question number to 0
        self.q_no = 0
        
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
        
        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected = IntVar()
        
        self.opts = self.radio_buttons()
        
        # display options for the current question
        self.display_options()
        
        # displays the button for next and exit.
        self.buttons()
        
        # no of questions
        self.data_size = len(question)
        
        # keep a counter of correct answers
        self.correct = 0

    def display_result(self):
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        print("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        # checks for if the selected option is correct
        if q_no < len(answer):
            if self.opt_selected.get() == answer[q_no]:
                return True
        return False      
    

    def next_btn(self):

        
    
        if self.check_ans(self.q_no):
        # if the answer is correct it increments the correct by 1
            self.correct += 1

    # Moves to next Question by incrementing the q_no counter
        self.q_no += 1

        if self.q_no == self.data_size:
        # if it is the last question, change the text of the button to "SUBMIT"
            self.next_button.configure(text="SUBMIT")

        if self.q_no == self.data_size + 1:
        # if the submit button was clicked, display the result
            self.display_result()
        # destroy the GUI
            root.destroy()
        else:        # shows the next question
            self.display_question()
            self.display_options()

    def buttons(self):
        # The first button is the Next button to move to the
        # next Question
        self.next_button = Button(root, text="NEXT", command=self.next_btn, width=10, bg="#F2A30F", fg="white", font=("ariel", 16, "bold"))
        self.next_button.place(x=350, y=380)

        # This is the second button which is used to Quit the GUI
        quit_button = Button(root, text="Quit", command=root.destroy, width=10, bg="#F2A30F", fg="white", font=("ariel", 16, " bold"))
        quit_button.place(x=600, y=380)
        
    def select_option(self, event):
    # Toggle the selection of the radio button
        event.widget.invoke()
    # Set opt_selected to the value of the selected radio button
        self.opt_selected.set(event.widget.value)

        
    def display_options(self):
        self.opt_selected.set(-1)
        if self.q_no >= len(options):
            return
        val = 0
        for option in options[self.q_no]:
            radio_button = Radiobutton(root, text=option, value=val, variable=self.opt_selected, font=("ariel bold", 20),bg="white")
            radio_button.place(x=50, y=200 + val * 40)
            val += 1

            
    def radio_buttons(self):
        self.opt_selected = IntVar()
        return self.opt_selected
    
    def display_question(self):

        if self.q_no >= len(options):
            return

        ques = question[self.q_no]
        self.ques_label = Label(root, text=ques, font=("ariel bold", 20), bg='white')
        self.ques_label.place(x=50, y=150)
        
        
    def display_title(self):
        self.title = Label(root, text="Your Exam has been started",width=80, bg="#0b8", fg= "white",font=("ariel bold", 20, "bold"))
        self.title.place(x=0, y=2)
        

label2 = Label(root, text="Total:5",font=("ariel bold", 20, "bold"),bg="white")	      
label2.place(x=1000, y=45)

def start():
    global hours, minutes, seconds

    if hours == 4:
        return
    seconds -=1

    if seconds == 00:
        minutes -= 1
        seconds = 60
        
    if minutes == 00 and seconds == 00:
        hours = hours+1


    clock.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')

    root.after(1000, start)
clock = tk.Label(root, font=("bold",20), text="00:00:00",bg="white")
clock.place(x=1150,y=45)

label2 = Label(root, text="Total:5",font=("ariel bold", 20, "bold"),bg="white")	      
label2.place(x=1000, y=45)

hours,minutes,seconds=0,0,61

start()

quiz = Quiz()

root.after(60000,lambda:root.destroy())

root.mainloop()
