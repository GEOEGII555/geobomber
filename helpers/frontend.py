import os
import time
from . import strings
from enum import Enum

class FRONTENDTYPE(Enum):
    CONSOLE = 2
    PYTHONDIALOG = 1

currentFrontendType = FRONTENDTYPE.PYTHONDIALOG

try:
    from dialog import Dialog, DialogError
    d = Dialog()
    assert hasattr(d, "yesno")
except:
    raise
    currentFrontendType = FRONTENDTYPE.CONSOLE
    print(strings.FRONTEND_FALLING_BACK % ("Dialog", "Console"))

def invoke_with_resize_request(func, *args, **kwargs):
    if currentFrontendType == FRONTENDTYPE.PYTHONDIALOG:
        while True:
            try:
                return func(*args, **kwargs)
            except DialogError:
                print(strings.MAKE_TERMINAL_BIGGER)
                time.sleep(2)
    if currentFrontendType == FRONTENDTYPE.CONSOLE:
        return func(*args, **kwargs)
    raise NotImplementedError(f"Frontend {currentFrontendType.name} is not supported in invoke_with_resize_request()")

def yesno(question: str) -> bool:
    if currentFrontendType == FRONTENDTYPE.PYTHONDIALOG:
        return d.yesno(question)
    if currentFrontendType == FRONTENDTYPE.CONSOLE:
        print(question)
        answer = ""
        while answer != "y" and answer != "n":
            answer = input(strings.YESNO_PROMPT).lower()
        return answer == "y"
    raise NotImplementedError(f"Frontend {currentFrontendType.name} is not supported in yesno()")

def msgbox(message: str) -> None:
    if currentFrontendType == FRONTENDTYPE.PYTHONDIALOG:
        d.msgbox(message)
        return
    if currentFrontendType == FRONTENDTYPE.CONSOLE:
        print(message)
        input(strings.ENTER_CONTINUE)
        return
    raise NotImplementedError(f"Frontend {currentFrontendType.name} is not supported in msgbox()")

def menu(message: str, items: list) -> tuple:
    if currentFrontendType == FRONTENDTYPE.PYTHONDIALOG:
        return d.menu(message, choices=items)
    if currentFrontendType == FRONTENDTYPE.CONSOLE:
        print(message)
        valid_choices = []
        for x in items:
            valid_choices.append(x[0])
            print(f"{x[0]}: {x[1]}")
        choice = input("> ")
        while choice not in valid_choices:
            if choice == "":
                return ('esc', '')
            print(strings.INVALID_CHOICE)
            choice = input("> ")
        return ('ok', choice)
    raise NotImplementedError(f"Frontend {currentFrontendType.name} is not supported in menu()")

def progress(filepath: str):
    if currentFrontendType == FRONTENDTYPE.PYTHONDIALOG:
        return d.progressbox(file_path=filepath)
    if currentFrontendType == FRONTENDTYPE.CONSOLE:
        reutrn os.system(f"tail -f {filepath}")
    raise NotImplementedError(f"Frontend {currentFrontendType.name} is not supported in progress()")
