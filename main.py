import pydirectinput
import pygetwindow as gw
import time

def main():
    try:
        window = gw.getWindowsWithTitle('MapleRoyals May 31 2024 IMG')[0]
        window.activate()
        time.sleep(2)
        pydirectinput.press('c')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
