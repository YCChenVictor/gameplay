import pydirectinput
import pygetwindow as gw
import time

def check_hp():
    return 50

def check_mp():
    return 50

def heal():
    return

def attack():
    pydirectinput.press('c')

def focus_on_game():
    window = gw.getWindowsWithTitle('MapleRoyals May 31 2024 IMG')[0]
    window.activate()

def play():
    focus_on_game()
    time.sleep(2)
    while True:
        hp = check_hp()
        mp = check_mp()
        if hp < 50 or mp < 50:
            heal()
        attack()
        time.sleep(1)

def main():
    try:
        play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
