# hello_world.py
import pyautogui
import time

def main():
    print("Hello, World!")
    time.sleep(2)  # Wait for 2 seconds before pressing the key
    pyautogui.press('v')  # Simulate pressing the 'v' key

if __name__ == "__main__":
    main()
