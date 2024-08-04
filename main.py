import pydirectinput
import pygetwindow as gw
import time
from PIL import ImageGrab
import pytesseract
import queue

job_queue = queue.Queue()
game_window = None
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
hp_x, hp_y = 300, 790
mp_x, mp_y = 430, 790

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
        job_queue.put(lambda: check_hp(hp_x, hp_y))
        job_queue.put(lambda: check_mp(mp_x, mp_y))
        counter += 1
        if counter >= 200:
            job_queue.put(lambda: check_status())
            counter = 0
        job_queue.put(lambda: attack())

        job = job_queue.get()
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
