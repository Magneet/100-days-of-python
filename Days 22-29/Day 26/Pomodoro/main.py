from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
count = 0
def add_counter(count,num):
    count +=num
    return count



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width = 210, height=280, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="D:\GIT\\100-days-of-python\\Days 22-29\\Day 26\\Pomodoro\\tomato.png")
canvas.create_image(100, 150, image = photo)
canvas.create_text(100,130, text=count, fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.create_text(100,15, text="Timert", fill = GREEN, font=(FONT_NAME, 35, "bold"))

def exit_button():
    window.destroy()

def start_button():
    window.destroy()

def reset_button():
    window.destroy()


exit_button = Button(text="Exit", command=exit_button, width = 5, highlightthickness=0)
start_button = Button(text="Start", command=start_button, width = 5, highlightthickness=0)
reset_button = Button(text="Reset", command=reset_button, widt = 5, highlightthickness=0)
check_mark = Label(text="✔")


exit_button.place(x=150,y=300)
canvas.grid(column = 0, row = 0)
reset_button.place(x=150,y=270)
start_button.place(x=0,y=270)
check_mark.place(x=80,y=270)


window.mainloop()