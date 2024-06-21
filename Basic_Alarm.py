from tkinter import *
from tkinter import ttk
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x300")
root.title("Alarm Clock")

# Function to update the current time display
def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
        # Wait for one second
        time.sleep(1)
        
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            stop_button.pack(pady=10)

def stop_alarm():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    stop_button.pack_forget()

# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack(pady=10)

hour = StringVar(root)
hours = [f"{i:02d}" for i in range(24)]
hour.set(hours[0])

hour_label = Label(frame, text="Hour:", font=("Helvetica 12"))
hour_label.pack(side=LEFT)
hrs = ttk.Combobox(frame, textvariable=hour, values=hours, width=3, font=("Helvetica 12"))
hrs.pack(side=LEFT, padx=5)

minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(60)]
minute.set(minutes[0])

minute_label = Label(frame, text="Minute:", font=("Helvetica 12"))
minute_label.pack(side=LEFT)
mins = ttk.Combobox(frame, textvariable=minute, values=minutes, width=3, font=("Helvetica 12"))
mins.pack(side=LEFT, padx=5)

second = StringVar(root)
seconds = [f"{i:02d}" for i in range(60)]
second.set(seconds[0])

second_label = Label(frame, text="Second:", font=("Helvetica 12"))
second_label.pack(side=LEFT)
secs = ttk.Combobox(frame, textvariable=second, values=seconds, width=3, font=("Helvetica 12"))
secs.pack(side=LEFT, padx=5)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Label to display current time
time_label = Label(root, text="", font=("Helvetica 15"))
time_label.pack(pady=10)

# Stop alarm button
stop_button = Button(root, text="Stop Alarm", font=("Helvetica 15"), command=stop_alarm)

# Update current time every second
update_time()

# Execute Tkinter
root.mainloop()

