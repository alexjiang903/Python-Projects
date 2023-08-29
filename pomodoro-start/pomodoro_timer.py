from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    tomato_canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_display.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer_label
    work_sec = int(WORK_MIN*60)
    short_break_sec = int(SHORT_BREAK_MIN*60)
    long_break_sec = int(LONG_BREAK_MIN*60)
    reps += 1

    if reps % 8 == 0:
        timer_label.config(text= "Long break", fg=RED)
        count_down(long_break_sec)


    elif reps % 2 == 1:
        timer_label.config(text= "Working", fg=YELLOW)
        count_down(work_sec)
    

    else:
        timer_label.config(text= "Short break", fg=PINK)
        count_down(short_break_sec)
    
    

    
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"


    tomato_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = math.floor(reps/2)

        for i in range(work_sessions):
            checkmarks += "✓"
            if len(checkmarks) % 4 == 0:
                checkmarks = ""
        checkmark_display.config(text=checkmarks)    
    
    





    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=125, pady=75, bg=GREEN)


start_button = Button(text="Start", highlightbackground=GREEN, highlightthickness=0, command=start_timer)
reset_button = Button(text= "Reset", highlightbackground=GREEN, highlightthickness=0, command = reset_timer)
checkmark_display = Label(text="",font=(FONT_NAME, 14), bg=GREEN, fg=YELLOW)
timer_label = Label(text="Timer", font=(FONT_NAME, 48), bg=GREEN, fg=YELLOW)

tomato_canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_canvas.grid(row=1, column=1)
tomato_img = PhotoImage(file="tomato.png")
tomato_canvas.create_image(100, 112, image=tomato_img)
timer_text = tomato_canvas.create_text(100,130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))


start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_display.grid(row=3, column=1)
timer_label.grid(row=0, column=1)

window.mainloop()






