import win32gui, win32api, win32con
import time

hwnd = win32gui.FindWindow(None, 'BlueStacks')
hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
hwndChild2 = win32gui.GetWindow(hwndChild, win32con.GW_CHILD)

win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)

time.sleep(1)  # Without this delay, inputs are not executing in my case

win32api.PostMessage(hwndChild2, win32con.WM_KEYDOWN, win32con.VK_F1, 0)
time.sleep(.5)
win32api.PostMessage(hwndChild2, win32con.WM_KEYUP, win32con.VK_F1, 0)




if __name__ == '__main__':
    # Run Code blow


