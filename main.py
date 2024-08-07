import pydirectinput
import pygetwindow as gw
import time
from PIL import ImageGrab
import pytesseract
import queue
import random

job_queue = queue.Queue()
game_window = None
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
hp_x, hp_y = 300, 790
mp_x, mp_y = 430, 790

def press_keys_together(key1, key2):
    pydirectinput.keyDown(key1)
    pydirectinput.keyDown(key2)
    pydirectinput.keyUp(key2)
    pydirectinput.keyUp(key1)

def named_job(name, func):
    func.__name__ = name
    return func

def initialize_window():
    global game_window
    game_window = gw.getWindowsWithTitle('MapleRoyals May 31 2024 IMG')[0]

def is_blue(x, y):
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x, y))
    red, green, blue = pixel_color
    return blue > 200

def is_red(x, y):
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x, y))
    red, green, blue = pixel_color
    return red > 200

def move(direction):
    if direction == 'left':
        pydirectinput.press('left')
    elif direction == 'right':
        pydirectinput.press('right')

def check_hp(x, y):
    if not is_red(x, y):
        pydirectinput.press('t')

def check_mp(x, y):
    if not is_blue(x, y):
        pydirectinput.press('t')

def check_status():
    pydirectinput.press('a')
    time.sleep(1)
    pydirectinput.press('s')
    time.sleep(1)

def find_monsters():
    pass

def attack():
    # only when the monster is in range
    pydirectinput.press('c')

def focus_on_game():
    game_window.activate()

def play():
    job_queue.put(lambda: check_status())
    counter = 0
    while True: # add a command queue
        counter += 1
        if counter % 101 == 0:
            job_queue.put(named_job('check_status', lambda: check_status()))
        elif counter % 801 == 0:
            job_queue.put(named_job('feed pet', lambda: pydirectinput.press('y')))
        elif counter % 5 == 0:
            job_queue.put(named_job('check_hp', lambda: check_hp(hp_x, hp_y)))
            job_queue.put(named_job('check_mp', lambda: check_mp(mp_x, mp_y)))
        elif counter % 21 == 0:
            for _ in range(random.randint(4, 6)):
                job_queue.put(named_job('press_keys', lambda: press_keys_together('left', 'v')))
            for _ in range(random.randint(1, 3)):
                job_queue.put(named_job('press_kevys', lambda: press_keys_together('right', 'v')))
        elif counter % 31 == 0:
            job_queue.put(named_job('move_left', lambda: move('left')))
            job_queue.put(named_job('move_right', lambda: move('right')))
        else:
            job_queue.put(named_job('attack', lambda: attack()))

        job = job_queue.get()
        print(job.__name__)
        job()
        job_queue.task_done()

def main():
    initialize_window()
    focus_on_game()
    time.sleep(2)
    try:
        play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
