import pyautogui
import tkinter as tk
import time
import sys

# Define the list of positions to cycle through (adjust as needed)
positions = [
    (200, 100),  # Example position 1
    (500, 500),  # Example position 2
    (800, 300)   # Example position 3
]

current_position_index = 0

def move_mouse_and_press_key():
    global current_position_index
    
    # Get the next position from the list
    next_position = positions[current_position_index]
    
    # Move the mouse to the next position
    pyautogui.moveTo(next_position, duration=0.25)
    
    # Press the 'f13' key
    pyautogui.press('f13')
    
    # Update the current position index
    current_position_index = (current_position_index + 1) % len(positions)

def shutdown_countdown(shutdown_time_seconds):
    remaining_time = shutdown_time_seconds
    while remaining_time > 0:
        label.config(text=f"Shutting down in {remaining_time // 60} minutes and {remaining_time % 60} seconds")
        remaining_time -= 1
        root.update()
        time.sleep(1)
    root.destroy()
    sys.exit()

def set_shutdown_time():
    shutdown_time_minutes = entry.get()
    if shutdown_time_minutes:
        shutdown_time_seconds = int(shutdown_time_minutes) * 60
        shutdown_countdown(shutdown_time_seconds)

root = tk.Tk()
root.title("Set Shutdown Time")

label = tk.Label(root, text="Enter shutdown time (in minutes):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Shutdown", command=set_shutdown_time)
button.pack()

root.mainloop()

while True:
    move_mouse_and_press_key()
    time.sleep(30)  # Wait for 30 seconds before moving the mouse and pressing the key again
