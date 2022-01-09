# ---------------------------- DESCRIPTION ------------------------------- #
# Pomodoro App
# ------------
# 25min work, 5min break
# repeat the above 4 times
# 15 min break
# start from beginning

# ---------------------------- IMPORTS ------------------------------- #
import tkinter
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
    canvas.itemconfig(timer_text, text=f"00:00")
    header_label["text"] = "Timer"
    header_label["fg"] = GREEN
    checkmarks_label["text"] = ""
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        header_label["text"] = "Break"
        header_label["fg"] = RED
    elif reps % 2 == 0:
        count_down(short_break_sec)
        header_label["text"] = "Break"
        header_label["fg"] = PINK
    else:
        count_down(work_sec)
        header_label["text"] = "Work"
        header_label["fg"] = GREEN

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    seconds = count % 60
    minutes = int((count - seconds) / 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if count > 0:
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.Floor(reps / 2)
        checkmarks = ""
        for _ in range(work_sessions):
            checkmarks += "✔️"
        checkmarks_label["text"] = checkmarks

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="day-28-PomodoroApp/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1,column=1)

header_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"))
header_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

checkmarks_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, anchor="center", font=(FONT_NAME, 20, "bold"))
checkmarks_label.grid(row=3, column=1)

window.mainloop()
