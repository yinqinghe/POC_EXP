import pyautogui

pyautogui.FAILSAFE=False   
#是否启用自动防故障功能，默认这项功能为True,当鼠标指针在屏幕最左上方时程序报错！

pyautogui.PAUSE=1
#意味着所有的pyautogui指令都要停顿1秒；可以防止键盘鼠标操作太快

print(pyautogui.position())  

# pyautogui.moveTo(200,400,duration=2)
# print(pyautogui.position())  

#获取屏幕大小
width,height=pyautogui.size()
print(width,height)

# pyautogui.rightClick()    #鼠标当前位置右键单击
# pyautogui.leftClick()    #鼠标当前位置左键单击
#输入字符串
# pyautogui.typewrite("Hello World!")  #HelloWorld！
pyautogui.doubleClick(200,390,button='left')  #鼠标在(x,y)位置双击

pyautogui.click(200,390, clicks=1, interval=0.0, button='right', duration=1)
# pyautogui.click(200,400, clicks=1, interval=0.0, button='left/right/middle', duration=1)
#在(x,y)位置点击，clicks表示点击次数，interval表示单击间隔时间，button选择左键/右键/中键点击HelloWorld！HelloWorld！HelloWorld！Hello World!

pyautogui.hotkey('win',"d")

pyautogui.hotkey('win',"r")

pyautogui.typewrite("mstsc") 

#按下并松开某键
pyautogui.press("enter")

#按下和松开
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")

pyautogui.typewrite("110.110.110.110") 
