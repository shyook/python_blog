import pyautogui
import pyperclip

print("Hello, World")

print (pyautogui.size())

print (pyautogui.position())

pyautogui.moveTo(100, 200)
# pyautogui.moveTo(400, 600, 2)
# pyautogui.dragTo(300, 800, 2)
# pyautogui.click()hello worldhello world한글
# pyautogui.rightClick()
# pyautogui.doubleClick()

# pyautogui.moveTo(816, 60)

pyautogui.write('hello world')
pyautogui.write('hello world', 0.25)

pyperclip.copy("한글")
pyautogui.hotkey('command', 'v')

button5location = pyautogui.locateOnScreen('5.png')
print(button5location)
point = pg.center(button5location) # Box 객체의 중앙 좌표를 리턴합니다.
print(point)
