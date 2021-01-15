import pyautogui
import math 

print(f"Resolution: {pyautogui.size()}\n")

width, height = pyautogui.size()
center = ( int(width / 2) , int(height / 2) )
raduis = (min(height, width) / 2) * 0.5

try:
    while True:
        for i in range(0,365, 5):
            delta_y = int(raduis*math.sin(math.radians(i)))
            delta_x = int(raduis*math.cos(math.radians(i)))
            current_x = center[0] + delta_x
            current_y = center[1] + delta_y
            pyautogui.moveTo(current_x, current_y, 0.5)
            print(f"\tMove to :({current_x},{current_y})")
        pyautogui.press("shift")
        print("\n\t\t<====================================>\n")
except KeyboardInterrupt:
    print("\nKeyboard Interrupt!\n")

print(f"\t\tScript Done!\n")
