import mouse
import keyboard

from shutil import copy
import os

# Copying file in users directory
try:
    current = os.path.basename(__file__)
    new = "C:\\Users\\" + os.getlogin()
    copy(current,new)
except Exception as e:
    pass

# Define the movement step (you can adjust this as needed)
step = 10

# Function to move the mouse cursor
def move_cursor(x, y):
    current_x, current_y = mouse.get_position()
    mouse.move(current_x + x * step, current_y + y * step)

# Function to handle keyboard inputs
def on_press(event):
    if event.name == 'i':
        move_cursor(0, -1)
    elif event.name == 'k':
        move_cursor(0, 1)
    elif event.name == 'j':
        move_cursor(-1, 0)
    elif event.name == 'l':
        move_cursor(1, 0)
    elif event.name == 'u':
        mouse.click()
    elif event.name == 'o':
        mouse.right_click()
    elif event.name == 'y':
        mouse.wheel(1)
    elif event.name == 'p':
        mouse.wheel(-1)
    elif event.name == 'h':
        mouse.hold()
        
# printing commands 
print("\nMouse Controls:-\n  Move I,J,K,L\n  Click U,O Hold with H\n  Scroll Y,P")

# Register the callback function for key presses
keyboard.on_press(on_press)

# Keep the script running
keyboard.wait('esc')