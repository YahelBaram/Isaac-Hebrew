import pyperclip
import time

currentCopy = ""
while True:

    if(currentCopy != pyperclip.paste()):
        temp = pyperclip.paste().replace("\n", "").replace("\r", "")[::-1]
        if temp.endswith(" "):
            temp = temp[ : -1]
        pyperclip.copy(temp.replace(" ", "  ").replace("\n", ""))
        currentCopy = pyperclip.paste()
    time.sleep(1)