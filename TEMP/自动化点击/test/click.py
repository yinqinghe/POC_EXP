import pyautogui

pyautogui.FAILSAFE=False   
#是否启用自动防故障功能，默认这项功能为True,当鼠标指针在屏幕最左上方时程序报错！

pyautogui.PAUSE=1
#意味着所有的pyautogui指令都要停顿1秒；可以防止键盘鼠标操作太快

print(pyautogui.position())  


#获取屏幕大小
width,height=pyautogui.size()
print(width,height)


pyautogui.hotkey('win',"d")

pyautogui.hotkey('win',"r")

pyautogui.typewrite("mstsc") 

#按下并松开某键
pyautogui.press("enter")

#按下和松开
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")

pyautogui.typewrite("110.110.110.110") 
