import pydirectinput
import pygetwindow as gw
import time
from PIL import ImageGrab
import pytesseract

game_window = None

def initialize_window():
    global game_window
    game_window = gw.getWindowsWithTitle('MapleRoyals May 31 2024 IMG')[0]

def check_hp():
    bbox = (game_window.left, game_window.top, game_window.right, game_window.bottom)
    screenshot = ImageGrab.grab(bbox)
    hp_region = screenshot.crop((100, 100, 200, 120))
    hp_text = pytesseract.image_to_string(hp_region, config='--psm 7')
    try:
        hp_value = int(hp_text.strip())
    except ValueError:
        hp_value = 0
    return hp_value

def check_mp():
    return 50

def heal():
    return

def attack():
    pydirectinput.press('c')

def focus_on_game():
    game_window.activate()

def play():
    initialize_window()
    time.sleep(2)
    while True:
        hp = check_hp()
        print(hp)
        # mp = check_mp()
        # if hp < 50 or mp < 50:
        #     heal()
        # attack()
        time.sleep(1)

def main():
    try:
        play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
