import pyautogui
import time

# Define the list of positions to cycle through (adjust as needed)
positions = [
    (100, 100),  # Example position 1
    (500, 500),  # Example position 2
    (800, 300)  # Example position 3
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

while True:
    move_mouse_and_press_key()
    time.sleep(10)  # Wait for 10 seconds before moving the mouse and pressing the key again
